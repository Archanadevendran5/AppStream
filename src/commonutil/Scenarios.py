from src.commonutil.Locators import *
from src.commonutil.Actions import *


def clearCookies():
    try:
        if elementPresence(all_cookies, 10):
            logs.info("Cookies PopUp clearing method - Started")
            doClick(all_cookies)
            waitTime(2)
            doClick(dismiss)
            logs.info("Cookies PopUp clearing method - Completed")
    except Exception as e:
        logs.error("Exception occurred while clearing cookies: ", e)
        return False


def loginAWS(link):
    try:
        driver.get(link)
        logs.info("IAM Authentication: Initiated")
        waitTime(5)
        doClick(selectIAMUser)
        logs.info("IAM Authentication: User Selected")
        waitTime(2)
        if isDisplayed(confirmation_of_iam_user):
            pass
        else:
            logs.info("IAM Authentication: User ReSelected")
            doClick(selectIAMUser)
        waitTime(2)
        doClick(account_id)
        logs.info(f"IAM Authentication: Typing AccountID: '{ACCOUNTID}'")
        sendKeys(account_id, ACCOUNTID)
        doClick(login_next_button)
        elementPresence(username, 30)
        logs.info(f"IAM Authentication: Typing Username: '{USERNAME}'")
        sendKeys(username, USERNAME)
        waitTime(2)
        logs.info(f"IAM Authentication: Typing Password: '{PASSWORD}'")
        sendKeys(password, PASSWORD)
        waitTime(2)
        doClick(sign_in_button)
        elementPresence(ib_time_created_header, 30)
        logs.info("IAM Authentication: AWS Console Logged in Successfully")
        clearCookies()
    except Exception as e:
        logs.error("Exception occurred while logging into AWS: ", e)
        return False


def SortTheHeader(header):
    try:
        i = 2
        while (elementPresence(header, 5)) and i <= 2:
            doClick(header)
            waitTime(2)
            i += 1
        logs.info("Header - Time created Sorted set to descending order")
    except Exception as e:
        logs.error("Exception occurred while Sorting the header: ", e)
        return False


def deletingFleet():
    try:
        logs.info("Start proceeding deleting function")
        doClick(action_button)
        logs.info("Action button clicked")
        doClick(action_delete_button)
        logs.info("Action: Delete button clicked")
        if elementPresence(fleet_pop_delete_button, 10):
            doClick(fleet_pop_delete_button)
            logs.info("Delete button clicked in PopUp")
            waitTime(15)
        if elementPresence(success_toast, 10):
            logs.info("Fleet deleted Successfully")
    except Exception as e:
        logs.error("Exception occurred while deleting the fleets: ", e)
        return False


def disassociateStack():
    try:
        waitTime(5)
        if elementPresence(associate_stack_get_text, 5):
            element = getText(associate_stack_get_text)
            logs.info(f"Executing disassociate stack : '{element}'")
            doClick(associate_stack_get_text)
            logs.info(f"Redirecting to '{element}' stack page to disassociate")
            if elementPresence(action_button, 60):
                doClick(action_button)
                logs.info("Action button clicked")
                waitTime(3)
                doClick(disassociate_fleet)
                logs.info("Disassociate button clicked")
                waitTime(3)
                doClick(confirm_disassociate)
                logs.info("Disassociate pop up button clicked")
                if elementPresence(success_toast, 10):
                    goBackPage()
                    if elementPresence(fleet_status_get_text, 20):
                        logs.info("redirecting to Fleet page")
        else:
            logs.info("Stack is not Associated in fleet. So Skipping the disassociate stack function ")
            pass
    except Exception as e:
        logs.error("Exception occurred while disassociate the Stacks: ", e)
        return False


def fleetTypeVerification():
    try:
        fleetTypeText = getText(fleet_type_get_text)
        if fleet_type_get_text == "Elastic":
            doClick(ratio_button)
            waitTime(3)
            doClick(fleet_detail_open_pop_up)
            waitTime(3)
            logs.info(f"Executing application disassociate due to '{fleetTypeText}' fleet type")
            doClick(application_button)
            logs.info("Redirecting to Application tab")
            i = 0
            while elementPresence(application_ratio_button, 5) and i < 20:
                doClick(application_ratio_button)
                logs.info("Application selected")
                waitTime(2)
                doClick(disassociate_application)
                waitTime(5)
                doClick(disassociate_application_pop_up)
                logs.info("Application disassociate popup selected")
                i += 1
                if elementPresence(disassociate_application_toast, 5):
                    logs.info("Application dissociated successfully ")
                    continue
                else:
                    assert False
            logs.info("All applications disassociated successfully")
            waitTime(5)
            doClick(detail_button)
        else:
            logs.info(f"Skipping application disassociate due to '{fleetTypeText}' fleet type")
            doClick(ratio_button)
            waitTime(5)
            doClick(fleet_detail_open_pop_up)
            pass
    except Exception as e:
        logs.info("Exception occurred while executing disassociate the application: ", e)
        return False


def deleting_fleet():
    try:
        fleetStatusGetText = getText(fleet_status_get_text)
        logs.info(f"Status of the Fleet is '{fleetStatusGetText}'")
        if fleetStatusGetText == "Stopping":
            i = 0
            while fleetStatusGetText != "Stopped" and i < 20:
                waitTime(30)
                driver.refresh()
                logs.info("Page getting refresh")
                if elementPresence(fleet_status_get_text, 20):
                    fleetStatusGetText = getText(fleet_status_get_text)
                    logs.info(f"printing the status '{fleetStatusGetText}'")
                    pass
                clearCookies()
                i += 1
        if fleetStatusGetText == "Running":
            logs.info(f"Execution initiated to change the Fleet status to 'Stop' ")
            doClick(action_button)
            logs.info("Action button clicked")
            doClick(action_stop_button)
            logs.info("Action Stop button clicked")
            doClick(stop_button_pop_up)
            logs.info("Action Stop button pop-up clicked")
            i = 0
            while fleetStatusGetText != "Stopped" and i < 20:
                logs.info(fleetStatusGetText)
                waitTime(30)
                driver.refresh()
                if elementPresence(fleet_status_get_text, 20):
                    fleetStatusGetText = getText(fleet_status_get_text)
                    logs.info(f"printing the status '{fleetStatusGetText}'")
                    pass
                clearCookies()
                i += 1
            logs.info("Fleet status changed to 'Stopped'")
            if fleetStatusGetText == "Stopped":
                deletingFleet()
            else:
                assert False
        elif fleetStatusGetText == "Stopped":
            deletingFleet()
        elif fleetStatusGetText == "Starting":
            assert False
    except Exception as e:
        logs.info("Exception occurred while deleting the fleets: ", e)
        return False


def StopImageBuilder():
    try:
        load = 0
        logs.info("Image Builder: Found Stop Button")
        doClick(action_stop_button)
        logs.info("Image Builder: Stop Button Clicked and waiting until the Image Builder Stops")
        while elementPresence(stopping, 20) and load <= 100:
            logs.info("Image Builder: Waiting 30sec for next refresh")
            waitTime(30)
            doClick(refresh_button)
        logs.info("ImageBuilder : Stopped")
        waitTime(10)
        logs.info("Image Builder: Page refreshing")
        driver.refresh()
        clearCookies()
        doClick(ratio_button)
        waitTime(2)
        doClick(action_button)
    except Exception as e:
        print("Exception occurred while executing StopImageBuilder: ", e)
        return False


def DeleteImageBuilder():
    try:
        load = 0
        if elementPresence(action_delete_button, 5):
            logs.info("Image Builder: Found Delete Button")
            doClick(action_delete_button)
            waitTime(2)
            doClick(pop_delete_button)
            while elementPresence(deleting, 20) and load <= 100:
                waitTime(5)
                doClick(refresh_button)
            logs.info("Image Builder: Deleted")
    except Exception as e:
        print("Exception occurred while executing DeleteImageBuilder: ", e)
        return False
