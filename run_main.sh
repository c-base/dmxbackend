#!/bin/bash

source .venv/bin/activate
python ./main.py \
	tests/mainhall_2026_011_cven.qxw tests/mainhall_2026_011_cven.ini \
	--usb /dev/serial/by-id/usb-ENTTEC_DMX_USB_PRO_EN080082-if00-port0 --outgoing 10.0.1.143 --port 8000
# was 10.0.1.143 - deactivated for cven by uk
