#!/bin/bash

source ~/.virtualenvs/dmxbackend/bin/activate
python ./main.py tests/mainhall_2017_010.qxw --usb /dev/ttyUSB0
