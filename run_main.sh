#!/bin/bash

source .venv/bin/activate
python ./main.py tests/tests/mainhall_2025_ALL_008_FediDayrcven.qxw tests/tests/mainhall_2025_ALL_008_FediDayrcven.ini \
        --usb /dev/serial/by-id/usb-ENTTEC_DMX_USB_PRO_EN080082-if00-port0 \
        --second-usb /dev/serial/by-id/usb-ENTTEC_DMX_USB_PRO_EN080067-if00-port0 \
        --port 8000
