import asyncio
import time
import logging
import serial
from typing import List
from pyftdi.ftdi import Ftdi

from . import channel_state


log = logging.getLogger(__name__)



class OpenDMXProtocol(asyncio.Protocol):

    def __init__(self, *args, **kwargs):
        # Device information
        self.__ftdi_vendor_id = kwargs.pop("ftdi_vendor_id", 0x0403)
        self.__ftdi_product_id = kwargs.pop("ftdi_product_id", 0x6001)
        self.__ftdi_serial = kwargs.pop("ftdi_serial", None)

        # Store the device
        self.__ftdi = None

        super().__init__()

    def connection_made(self, transport):
        self.transport = transport
        channel_state.subscribe_dmx(self.notify_dmx)
        log.info('Serial port opened: %s' % transport)
        transport.serial.rts = False

    def data_received(self, data):
        log.debug('Serial data received: %s' % repr(data))
        # self.transport.close()

    async def notify_dmx(self):
        dmx = channel_state.as_dmx()
        self.send_dmx(dmx)

    def send_dmx(self, dmx):
        self._transmit(dmx)

    def connection_lost(self, exc):
        self._close()
        log.info('Serial port closed')
        asyncio.get_event_loop().stop()

    def _connect(self):
        # Try to close if exists
        if self.__ftdi is not None:
            try:
                self.__ftdi.close()
            except Exception:
                pass

        # Get new device
        self.__ftdi = Ftdi()
        self.__ftdi.open(self.__ftdi_vendor_id, self.__ftdi_product_id, serial=self.__ftdi_serial)
        self.__ftdi.reset()
        self.__ftdi.set_baudrate(baudrate=250000)
        self.__ftdi.set_line_property(bits=8, stopbit=2, parity='N', break_=False)

    def _close(self):
        self.__ftdi.close()
        print("CLOSE: OpenDMX closed")

    def _transmit(self, frame: List[int], first: int):
        # Convert to a bytearray and pad the start of the frame
        # We're transmitting direct DMX data here, so a frame must start at channel 1, but can end early
        data = bytearray(([0] * (first - 1)) + frame)

        # The first byte in the type, and is `0` for normal DMX data
        data.insert(0, 0)

        # Write
        self.__ftdi.set_break(True)
        self.__ftdi.set_break(False)
        self.__ftdi.write_data(data)


if __name__ == '__main__':
    ser = serial.Serial('/dev/tty.usbserial-EN080082')
    print(ser.name)  # check which port was really used

    for i in range(250):
        test_data = bytearray(512)
        test_data[0] = 11
        test_data[1] = 255# random.randint(50, 250)
        test_data[2] = 10# random.randint(50,250)
        msg = test_data
        # print([int(x) for x in msg])
        print("is open? %s" % ser.is_open)
        res = ser.write(msg)  # write a string
        print("%s is out" % res)
        ser.flush()
        time.sleep(0.02)
    time.sleep(0.5)
    ser.close()
