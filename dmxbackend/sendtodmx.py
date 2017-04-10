#!/usr/bin/python2.6

import socket


class ArtNetError(Exception):
    def __init__(self, message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = message


class ArtNet(object):
    def __init__(self, broadcast="255.255.255.255"):
        self._udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self._broadcast = broadcast

    def send(self, packet):
        if packet:
            print("====")
            #print(packet)
            sendData = self._udp.sendto(packet, 0, (self._broadcast, 6454))
            self._udp.close()
            if sendData == len(packet):
                return True
            else:
                return False
        else:
            return False

    def build_dmx_header(self):
        # A DMX packet contains 512 bytes of DMX data every time.
        header = bytearray()
        # id
        header.extend(bytearray(b'Art-Net'))
        header.append(0x0)
        # OP-Code low byte first
        header.append(0x00)
        header.append(0x50)
        # proto ver high byte first
        header.append(0x0)
        header.append(14)
        # sequence 
        header.append(0x0)
        # physical port
        header.append(0x0)
        # universe low byte first
        header.append(0x0)
        header.append(0x0)
        # length high byte first
        header.append((512 >> 8) & 0xFF)
        header.append(512 & 0xFF)
        return header

    def send_dmx(self, dmx):
        if (len(dmx) > 512):
            raise ArtNetError("dmx packet > 512")
        plain_dmx = bytearray(512)
        for i in range(len(plain_dmx)):
            plain_dmx[i] = 0x10
        for i in range(len(dmx)):
            plain_dmx[i] = dmx[i]
        packet = self.build_dmx_header()
        packet.extend(plain_dmx)
        return self.send(packet)

    def send_light_list(self, lightList):
        dmxdata = bytearray(512)
        for light in lightList:
            # dmxchannel 1 = dmxdata[0]
            # dmxchannel 512 = dmxdata[511]
            offset = light['channel']
            dmxdata[offset-1] = light['red']
            dmxdata[offset] = light['green']
            dmxdata[offset+1] = light['blue']
            # light : map of red,blue,green,channel,channeloffset,name,x,y,radius,channelsize
        return self.send_dmx(dmxdata)


if __name__ == '__main__':
    artnet = ArtNet(broadcast='10.0.1.133')
    dmx = bytearray()
    fh = open("dmx.dat", 'r')
    for i in fh.readlines():
        dmx.append(int(i))
    artnet.send_dmx(dmx)

    # load file
    # prepare to send
