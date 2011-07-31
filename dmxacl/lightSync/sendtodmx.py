#!/usr/bin/python2.6

import socket

class ArtNet(object):
    def __init__(self, broadcast="2.255.255.255"):
        self.__udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__udp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.__broadcast = broadcast

    def __send(self, packet):
        if packet:
            sendData = self.__udp.sendto(packet, 0, (self.__broadcast, 6454))
            if sendData == len(packet):
                return True
            else:
                return False
        else:
            return False

    def buildDMXHeader(self):
        # a dmx packet contains every time 512 bytes dmx data
        header = bytearray()
        # id
        header.extend(bytearray(b'Art-Net'))
        header.append(0x0)
        # opcode low byte first
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

    def sendToDmx(self, dmx):
        if (len(dmx) > 512):
            raise RunTimeError("dmx packet > 512")
        plainDmx = bytearray(512)
        for i in range(len(dmx)):
            plainDmx[i] = dmx[i]
        packet = self.buildDMXHeader()
        packet.extend(plainDmx)
        return self.__send(packet)

    def sendListToDMX(self, lightList):
        dmxdata = bytearray(512)
        for light in lightList:
            # dmxchannel 1 = dmxdata[0]
            # dmxchannel 512 = dmxdata[511]
            offset = light['channel']
            dmxdata[offset] = light['red']
            dmxdata[offset+1] = light['green']
            dmxdata[offset+2] = light['blue']
            # light : map of red,blue,green,channel,channeloffset,name,x,y,radius,channelsize
        return self.sendToDmx(dmxdata)


if __name__ == '__main__':
    artnet = ArtNet(broadcast='10.0.1.133')
    dmx = bytearray()
    fh = open("dmx.dat", 'r')
    for i in fh.readlines():
        dmx.append(int(i))
    artnet.sendToDmx(dmx)

    # load file
    # prepare to send
