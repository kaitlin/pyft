# PyFT
(prounounced "pfft")

PyFT is a python API wrapper around the Financial Times Content API, v2. Access to the Financial Times API requires a key, which can be obtained at [developer.ft.com](http://developer.ft.com).

## Dependencies

This wrapper is written to be compatible with Python 3+. To install necessary dependencies, use [pip](https://pypi.python.org/pypi/pip) and the provided `requirements.txt` file.

`pip install -r requirements.txt`

## Getting Started

PyFT will look in two places for your api key. First, `~/.ft.key` will be read and the contents of that file will be used for your API key. Secondly, PyFT will try to use an environment variable called `FT_API_KEY`. If the environment variable is present, it will override the contents of the file. 
