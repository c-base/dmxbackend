import asyncio
import serial.aio
import time
import logging

from . import channel_state

log = logging.getLogger(__file__)

def create_enttec_dmx_message(dmx_bytes:bytearray):
    if len(dmx_bytes) != 512:
        raise Exception("len(dmx_bytes) != 512")

    b = bytearray(518)
    b[0] = 0x7e

    # function
    b[1] = 0x06

    # payload length, low byte first
    b[2] = 513 & 0xff
    b[3] = 513 >> 8

    # payload with DMX start byte
    b[4] = 0x00
    b[5:517] = dmx_bytes
    b[517] = 0xe7

    return b


class EnttecProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        channel_state.subscribe(self.notify_dmx)
        log.info('Serial port opened: %s' % transport)
        transport.serial.rts = False

    def data_received(self, data):
        log.debug('Serial data received: %s' % repr(data))
        # self.transport.close()

    async def notify_dmx(self):
        dmx = channel_state.as_dmx()
        self.send_dmx(dmx)

    def send_dmx(self, dmx):
        message = create_enttec_dmx_message(dmx)
        self.transport.write(message)

    def connection_lost(self, exc):
        log.info('Serial port closed')
        asyncio.get_event_loop().stop()


if __name__ == '__main__':
    ser = serial.Serial('/dev/tty.usbserial-EN080082')
    print(ser.name)  # check which port was really used

    for i in range(250):
        test_data = bytearray(512)
        test_data[0] = 11
        test_data[1] = 255# random.randint(50, 250)
        test_data[2] = 10# random.randint(50,250)
        msg = create_enttec_dmx_message(test_data)
        # print([int(x) for x in msg])
        print("is open? %s" % ser.is_open)
        res = ser.write(msg)  # write a string
        print("%s is out" % res)
        ser.flush()
        time.sleep(0.02)
    time.sleep(0.5)
    ser.close()

