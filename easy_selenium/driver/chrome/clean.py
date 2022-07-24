from termcolor import colored
from colorama import init
import os
import platform
import subprocess


from ..utils import BASE_PATH


DRIVER = BASE_PATH / "executable"
init()


class Clean:
    def update_binary(self, path):
        word = "cdc_".encode()
        new = "tch_".encode()
        path = path
        while True:
            string = b""
            Flag = 0
            with open(path, "r+b") as file:
                pos = 0
                data = string = file.read(1)
                while data:
                    data = file.read(1)
                    if data == b" ":
                        if word in string:
                            new_tring = string.decode().replace(
                                word.decode(), new.decode()
                            )
                            file.seek(pos)
                            file.write(new_tring.encode())
                            Flag = 1
                            break
                        else:
                            pos = file.tell()
                            data = string = file.read(1)
                    else:
                        string += data
                        continue
            if not Flag:
                break

    def remove_signature_in_javascript(self, chromedriver):
        try:
            if platform.system() == "Windows":
                os.chmod(chromedriver, 755)
            else:
                os.chmod(chromedriver, 777)
                subprocess.Popen(f"sudo chmod 777 {chromedriver}", stdout=subprocess.PIPE, shell=True)
            with open(chromedriver, "r", errors="ignore") as chrome:
                content = chrome.read()
            content = content.replace("cdc_", "tch_")
            self.update_binary(chromedriver)
        except Exception as error:
            print(colored("[-] Signature: ", "red") + str(error))
