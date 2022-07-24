<div align="center">
<img src="https://github.com/SelmiAbderrahim/easy-selenium/blob/master/easy_selenium/screenshots/easy.png?raw=true" width="200">
<p>A list of functionalities that makes working with Selenium much easier.</p>
</div>


## Requirements

- Chrome or Firefox
- Python 3.7+

## Installation

```
pip install easy-py-selenium
```

## TOC

- [Create Undetectable Chrome Driver](#create-undetectable-chrome-driver)
  - [Features:](#features)
  - [Passed the antibot test ](#passed-the-antibot-test-)
  - [Usage](#usage)
  - [Options](#options)
- [Remote browser (debugging mode)](#remote-browser-debugging-mode)
  - [Features](#features-1)
  - [Usage](#usage-1)
  - [Options](#options-1)
- [Create Firefox Driver (Geckodriver)](#create-firefox-driver-geckodriver)
  - [Features:](#features-2)
  - [Usage](#usage-2)
  - [Options](#options-2)
- [Easy authentication](#easy-authentication)
- [Cookies](#cookies)
  - [Example](#example)
- [Utility functions](#utility-functions)
  - [Mimic real user input](#mimic-real-user-input)
  - [Driver safe quit](#driver-safe-quit)
  - [Send emails through Gmail](#send-emails-through-gmail)
  - [Scrolling](#scrolling)
  - [userAgent](#useragent)
  - [Screenshots](#screenshots)
- [Logging](#logging)
- [Testing](#testing)
  - [Installation](#installation-1)
  - [Downlaod the project](#downlaod-the-project)
  - [Environment variables](#environment-variables)



<br>
<br>

---

<br>
<br>

# Create Undetectable Chrome Driver

easy-selenium will download and patch a Chrome driver to make it undetectable. So that you can use an undetectable Chrome driver for your Python Selenium code.

## Features:

- Download the exact chrome driver based on your OS and installed chrome version.

- Remove browser control flag

- Remove signature in javascript

- Set User-Agent

- Use maximum resolution

- Run Chrome driver on headless mode.

- Unmute the sounds of the browser.


## Passed the antibot test [](https://bot.sannysoft.com)

![](https://github.com/SelmiAbderrahim/easy-selenium/blob/master/easy_selenium/screenshots/antibot-tested.png?raw=true)

## Usage

```

from easy_selenium.driver.chrome.driver import Driver
driver = Driver()
chrome = driver.create()

chrome.get("https://selmi.tech")

```

## Options

**Load Profile**

Launch Chrome with its default or custom profile so that you can use cookies and site preferences from that profile.

```
chrome = driver.create_driver(profile="")
```

Note: Make sure to provide the absolute path of your profile and if the given profile folder doesn't exist, it'll be created.

To find path to your chrome profile data you need to type chrome://version/ into address bar . 

![](https://github.com/SelmiAbderrahim/easy-selenium/blob/master/easy_selenium/screenshots/chrome-version-check.png?raw=true)

**Headless**

We can use a headless chrome browser to lower memory overhead and faster execution for the scripts that we write.

```
chrome = driver.create_driver(headless=False)
```

<br>
<br>

---

<br>
<br>


# Remote browser (debugging mode)

It launches a new Chrome session from a new Terminal (cmd) window on a given port number and profile path. It allows you to control an existing Chrome session.
 

## Features

- Open Chrome Instance on debugging mode

- Control an existing Chrome instance.

- Save/ load Chrome profiles.

## Usage

```
from easy_selenium.driver.chrome.driver import Remote
remote = Remote()
chrome = remote.create()

chrome.get("https://selmi.tech")

```

## Options

**Control an existing Chrome session**

Make sure that the session is up and running.
Remined: 
 - Windows: 
   - ``` chrome.exe --remote-debugging-port=9000 ```
 - Linux/ Mac: 
   - ``` /usr/bin/google-chrome --remote-debugging-port=9000 ```

```
from easy_selenium.driver.chrome.driver import Remote
remote = Remote()
chrome = remote.create(control_existing_instance=True, debug_port=9000)
```

**Launch a new Chrome session and save cookies in a folder (profile)**

To use a custom profile, put the its path in profile_path, and make sure to use the absolute path.
```
from easy_selenium.driver.chrome.driver import Remote
remote = Remote()
chrome = remote.create(profile="C:\path")
```

<br>
<br>

---

<br>
<br>


# Create Firefox Driver (Geckodriver)

easy-selenium will download and launch Geckodriver. But it will be detected as bot.

## Features:

- Download the exact the latest geckodriver.

- Set User-Agent

- Use maximum resolution

- Run geckodriver on headless mode.

- Unmute the sounds of the browser.



## Usage

```

from easy_selenium.driver.firefox.driver import Driver
driver = Driver()
firefox = driver.create()

firefox.get("https://selmi.tech")

```

## Options

**Load Profile**

Launch Firefox with its default or custom profile so that you can use cookies and site preferences from that profile.

```
firefox = driver.create_driver(profile="")
```

Note: Make sure to provide the absolute path of your profile.

For Windows users, you can find your profile path by pressing the Windows Key key and then start typing: %APPDATA%\Mozilla\Firefox\Profiles\




**Headless**

We can use a headless Firefox browser to lower memory overhead and faster execution for the scripts that we write.

```
firefox = driver.create_driver(headless=False)
```


<br>
<br>

---

<br>
<br>

# Easy authentication

Automate the login process to a list of websites. Including:

- ## Linkedin

```
from easy_selenium.driver.chrome.driver import Driver
from easy_selenium.authentication.login.linkedin import Login
driver = Driver()
chrome = driver.create()
login = Login("example@gmail.com", "password")
login.start(chrome)
```

<br>
<br>

---

<br>
<br>


# Cookies

Get and set cookies with the Selenium methods get_cookies() and add_cookie()

## Example

**Save cookies**

```
from easy_selenium.cookies.cookies import Cookies
cookies = Cookies()
cookies.save(driver, url, cookies_file_name, cookies_folder_path=None)
```

**Load cookies**

```
from easy_selenium.cookies.cookies import Cookies
cookies = Cookies()
cookies.load(driver, url, cookies_file_name, cookies_folder_path=None)
```

<br>
<br>

---

<br>
<br>


# Utility functions

A list of functions that you might need when you use Selenium.

## Mimic real user input

Write texts in fields like a real human, send keys one by one.

```
from easy_selenium.common.funcs import send_keys_one_by_one
send_keys_one_by_one(controller, keys, min_delay=0.05, max_delay=0.25)
```

## Driver safe quit

When using headless browser, it's important to make sure that there are no unnecessary driver left running.
Set exit to False to avoid sys.exit() once the function is fired.

```
from easy_selenium.common.funcs import driver_safe_quit
driver_safe_quit(driver, exit=True)
```

## Send emails through Gmail

Many times I had to copy the same function in many Selenium projects.

```
from easy_selenium.common.funcs import send_gmail
send_gmail(message, sender, password, receiver)
```

## Scrolling

Keep scrolling until the end of the page

```
from easy_selenium.common.funcs import scoll_until_the_end
scoll_until_the_end(driver)
```

Scroll to an element

```
from easy_selenium.common.funcs import scroll_to
scroll_to(driver, element)
```
## userAgent

```
from easy_selenium.common.funcs import get_user_agent
get_user_agent(driver)
```

## Screenshots

**Page Screenshot**

```
from easy_selenium.common.funcs import page_screenshot
page_screenshot(driver, file_name)
```

**Element Screenshot**

```
from easy_selenium.common.funcs import element_screenshot
element_screenshot(driver, file_name)
```

<br>
<br>

---

<br>
<br>

# Logging


To make logging simple, I'm using [Loguru](https://github.com/Delgan/loguru).

<img alt="Loguru logo" src="https://raw.githubusercontent.com/Delgan/loguru/master/docs/_static/img/demo.gif">

Keep logging the same way:

```
from easy_selenium.logger import logger
```

<br>
<br>

---

<br>
<br>

# Testing

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

<br>
<br>

---

<br>
<br>

Was it **useful** ?

then ⭐it.

Thanks.
