[**← BACK**](../../README.md)

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
