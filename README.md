## What is Needed?

 - Python 3.6
 - USB-to-DMX-Adapter like this one: https://www.enttec.com/eu/products/controls/dmx-usb/dmx-usb-pro/
 
## How to run this backend?

```
[create and activate virtualenv]
$ pip install -r requirements.txt
$ python3.6 main.py /dev/ttyUSB0 /path/to/qxw_filename.qxw
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
curl -v --data 'file=@tests/Example.png' http://localhost:8080/
```

