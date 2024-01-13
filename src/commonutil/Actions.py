from src.Authentication.Midway import *
import time
from selenium.common.exceptions import TimeoutException


def findElement(value):
    try:
        driver.find_element(By.XPATH, value)
    except Exception as e:
        logs.error("Exception occurred while finding the elements: ", e)
        return False


def getText(value):
    try:
        return driver.find_element(By.XPATH, value).text
    except Exception as e:
        logs.error("Exception occurred while getting text: ", e)
        return False


def doClick(value):
    try:
        driver.find_element(By.XPATH, value).click()
        waitTime(2)
    except Exception as e:
        logs.error("Exception occurred while clicking the element: ", e)
        return False


def goBackPage():
    try:
        driver.back()
    except Exception as e:
        logs.error("Exception occurred while navigate to previous page: ", e)
        return False


def sendKeys(value, key):
    try:
        driver.find_element(By.XPATH, value).send_keys(key)
    except Exception as e:
        logs.error("Exception occurred while sending the values: ", e)
        return False


def elementPresence(value, wait) -> bool:
    try:
        waiting = WebDriverWait(driver, wait)
        element_locator = (By.XPATH, value)
        waiting.until(ec.visibility_of_element_located(element_locator))
        return True
    except TimeoutException:
        return False


def isDisplayed(value):
    try:
        if driver.find_element(By.XPATH, value).is_displayed():
            return True
        else:
            logs.info("Element not found")
            return False
    except Exception as e:
        logs.error("Exception occurred while displaying the elements: ", e)
        return False


def waitTime(wait):
    try:
        time.sleep(wait)
    except Exception as e:
        logs.error("Exception occurred while waiting: ", e)
        return False
