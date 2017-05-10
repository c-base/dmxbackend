#!/bin/bash

source ~/.virtualenvs/dmxbackend/bin/activate
python ./main.py tests/mainhall_2017_010.qxw tests/mainhall_2017_010.ini --usb /dev/ttyUSB0 --mqtt "10.0.1.17"
