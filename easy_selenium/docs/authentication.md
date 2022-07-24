[**← BACK**](../../README.md)

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