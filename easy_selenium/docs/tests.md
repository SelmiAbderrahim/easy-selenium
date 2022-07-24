[**← BACK**](../README.md)

I'm using [Pytest](https://docs.pytest.org). 
pytest requires: Python 3.7+ or PyPy3.

## Installation

```
pip install -U pytest
```

## Downlaod the project

```
git clone https://github.com/SelmiAbderrahim/easy-selenium
cd easy-selenium
```

## Environment variables

To do all the testing, create a '.env' file in your working directory with these values:

```
BACKTRACE=1 # (For debugging) 1 = True & 0 = False
LINKEDIN_EMAIL_ADDRESS=emial@example.com
LINKEDIN_PASSWORD=password
```

Otherwise uncomment the functions you want to exclude.

**Run tests**

```
pytest easy-selenium/tests/
```