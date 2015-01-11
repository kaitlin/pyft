# PyFT
(prounounced "pfft")

PyFT is a python API wrapper around the Financial Times Content API, v2. Access to the Financial Times API requires a key, which can be obtained at [developer.ft.com](http://developer.ft.com).

## Dependencies

This wrapper is written to be compatible with Python 3+. To install necessary dependencies, use [pip](https://pypi.python.org/pypi/pip) and the provided `requirements.txt` file.

`pip install -r requirements.txt`

## Getting Started

PyFT will look in two places for your api key. First, `~/.ft.key` will be read and the contents of that file will be used for your API key. Secondly, PyFT will try to use an environment variable called `FT_API_KEY`. If the environment variable is present, it will override the contents of the file. 


To get the data for a single piece of content on FT.com:
```
from pyft import FT

ft = FT()
# the id can be pulled from the slug url of an FT.com story
content = ft.get_content("6f2ca3d6-86f5-11e4-982e-00144feabdc0")
print(content)
```


To get all of the content that has been updated since a certain date (continuing from previous example):

```
updated_content = ft.get_content_notifications(updated_since="2015-01-01")
```

##Running Tests

You can run the tests in the home directory with the python unittest framework:

`python -m unittest tests.py`
