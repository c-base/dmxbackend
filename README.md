## What is Needed?

 - Python 3.6
 - USB-to-DMX-Adapter like this one: https://www.enttec.com/eu/products/controls/dmx-usb/dmx-usb-pro/
 
## How to run this backend?

```
[create and activate virtualenv]
$ pip install -r requirements.txt
$ python3.6 main.py /path/to/qxw_filename.qxw --usb /dev/ttyUSB0
```

If you just want to test the server without a USB-to-DMX converter

```
python3.6 main.py /tests/mainhall_2017_010.qxw
```



## How To Run Tests

```
$ pip install -r requirements.txt
$ pytest
```

## Upload an Image

You can upload a image (PNG or JPG). Each line in the image represents one frame in an animation.
When you upload the file the animation is played with a frame-rate of 25 fps.

```
curl -v --data 'file=@tests/Example.png' http://dmx/
```

## Update the State Using MQTT

With `mosquitto_sub -h c-beam -t "dmx-mainhall/+"` you get both the fixtures (dmx-mainhall/fixtures) and the current state (dmx-mainhall/current_state) of the lights. If you want to see the fixtures in a more human-readable format, go to: http://dmx.cbrp3.c-base.org/api/v1/fixtures/ .

```
mosquitto_pub -h c-beam -t "dmx-mainhall/state" -m '[{"channel_id": "dmx-1-1/rgb/r", "value": 128}, {"channel_id": "dmx-1-1/rgb/g", "value": 0}, {"channel_id": "dmx-1-1/rgb/b", "value": 128}]'
```

