from src.commonutil.SetUpSelenium import *
from src.commonutil.LogFormat import *
import time
from src.Authentication.Credential import *


def midway_cookie_capture():
    global expires, username, session_token
    MidwayConfigDir = os.path.join(os.path.expanduser("~"), ".midway")
    MidwayCookieJarFile = os.path.join(MidwayConfigDir, "cookie")
    fields = []
    keyfile = open(MidwayCookieJarFile, "r")
    for line in keyfile:
        # parse the record into fields (separated by whitespace)
        fields = line.split()
        if len(fields) != 0:
            # get the yubi session token and expire time
            if fields[0] == MIDWAYFIELD0:
                session_token = fields[6].replace("\n", "")
                expires = fields[4]
            # get the user who generated the session token
            elif fields[0] == MIDWAYFIELD1:
                username = fields[6].replace("\n", "")
    keyfile.close()

    if time.gmtime() > time.gmtime(int(expires)):
        raise SystemError("Your Midway token has expired. Run mwinit to renew")

    cookie = {"username": username, "session": session_token}
    return cookie


def run_midway():
    logs.info("Midway authentication: Initiated")
    cookie = midway_cookie_capture()
    driver.get(MIDWAYLOGIN)
    cookie_dict1 = \
        {
            'domain': MIDWAYDOMAIN,
            'name': 'user_name',
            'value': cookie['username'],
            'path': '/',
            'httpOnly': False,
            'secure': True
        }
    cookie_dict2 = \
        {
            'domain': MIDWAYDOMAIN,
            'name': 'session',
            'value': cookie['session'],
            'path': '/',
            'httpOnly': True,
            'secure': True
        }

    midway_url = MIDWAYLINK
    driver.add_cookie(cookie_dict1)
    driver.add_cookie(cookie_dict2)

    match = False
    while not match:
        driver.get(midway_url)
        if driver.current_url == MIDWAYLINK:
            match = True
        time.sleep(1)
        driver.refresh()
    driver.refresh()
    logs.info("Midway authentication: Completed")
    time.sleep(3)
