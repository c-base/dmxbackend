## What is Needed?

 - Python 3.4+
 - aiohttp

## How To Run Tests

```
$ pip install -r requirements.txt
$ pytest
```

## Upload PNG
```
curl -v --data 'file=@tests/Example.png' http://localhost:8080/png_upload/
```

