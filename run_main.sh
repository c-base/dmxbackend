#!/bin/bash

source .venv/bin/activate
python ./main.py tests/mainhall_2025_ALL_006.qxw tests/mainhall_2025_ALL_006.ini \
        --usb /dev/serial/by-id/usb-ENTTEC_DMX_USB_PRO_EN080082-if00-port0 \
        --second-usb /dev/serial/by-id/usb-ENTTEC_DMX_USB_PRO_EN080067-if00-port0 \
        --port 8000
