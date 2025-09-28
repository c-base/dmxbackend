#!/bin/bash

source .venv/bin/activate
python ./main.py tests/mainhall_2025_ALL_006.qxw tests/mainhall_2025_ALL_006.ini --usb /dev/ttyUSB0 --port 8000
