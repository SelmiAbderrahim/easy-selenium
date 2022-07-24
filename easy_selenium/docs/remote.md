[**← BACK**](../../README.md)

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