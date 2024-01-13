from src.commonutil.Scenarios import *


def fleets():
    try:
        loginAWS(FLEETLINK)
        SortTheHeader(fleet_time_created_header)
        logs.info(f"Fleets: Total number of Iteration set is {ITERATION}")
        Execution = 0
        while elementPresence(ratio_button, 30) and Execution < int(ITERATION):
            logs.warning(f"---------- Iteration {Execution + 1} started -----------")
            fleetTypeVerification()
            waitTime(3)
            disassociateStack()
            waitTime(3)
            deleting_fleet()
            waitTime(20)
            doClick(fleet_detail_close_pop_up)
            waitTime(10)
            logs.warning(f"********** Iteration {Execution + 1} Completed **********")
            Execution += 1
        waitTime(20)
        logs.info(f"Fleets: {ITERATION} iteration completed")
    except Exception as e:
        logs.info("Exception occurred while deleting the fleets: ", e)
        return False
