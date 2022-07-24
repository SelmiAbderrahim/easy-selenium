[**← BACK**](../../README.md)

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