[**← BACK**](../../README.md)

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