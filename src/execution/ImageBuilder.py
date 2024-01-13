from src.commonutil.Scenarios import *


def imageBuilder():
    try:
        loginAWS(IMAGEBUILDERLINK)
        SortTheHeader(ib_time_created_header)
        logs.info(f"Image Builder: Total number of Iteration set is {ITERATION}")
        Execution = 0
        while elementPresence(ratio_button, 30) and Execution < int(ITERATION):
            logs.warning(f"---------- Iteration {Execution + 1} started ----------")
            waitTime(10)
            doClick(ratio_button)
            waitTime(2)
            doClick(action_button)
            logs.info("Image Builder: Action button clicked")
            waitTime(2)
            if elementPresence(delete_disabled_button, 5):
                StopImageBuilder()
                DeleteImageBuilder()
            else:
                DeleteImageBuilder()
            waitTime(5)
            logs.warning(f"********** Iteration {Execution + 1} Completed **********")
            Execution += 1
        waitTime(20)
        logs.info(f"Image Builder: {ITERATION} iteration completed")
        driver.quit()
    except Exception as e:
        print("Exception occurred while executing ImageBuilder: ", e)
        return False
