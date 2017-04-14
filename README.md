## What is Needed?

 - Python 3.6
 
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

## Upload PNG
```
curl -v --data 'file=@tests/Example.png' http://localhost:8080/
```

