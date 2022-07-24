# import sys
# from decouple import UndefinedValueError
# from decouple import config
# try:
#     sys.path.append("..")
#     from ..driver.chrome.driver import Driver
#     from ..authentication.login.linkedin import Login as LN
# except ImportError:
#     sys.path.append(".")
#     from ..driver.chrome.driver import Driver
#     from ..authentication.login.linkedin import Login as LN


# def test_linkedin_login():
#     try:
#         username = config("LINKEDIN_EMAIL_ADDRESS")
#         password = config("LINKEDIN_PASSWORD")
#     except UndefinedValueError:
#         assert False
#     else:
#         driver = Driver()
#         login = LN(username, password)
#         chrome = driver.create(headless=True)
#         assert login.start(chrome)
#         chrome.quit()
