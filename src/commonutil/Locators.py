
# Login Page
selectIAMUser = "//*[@id='iam_user_radio_button']"
account_id = "//*[@id='resolving_input']"
login_next_button = "//*[@id='next_button']"
username = "//*[@id='username']"
password = "//*[@id='password']"
sign_in_button = "//*[@id='signin_button']"

# Image Builder
ib_time_created_header = "//th[5]/div/div"
ratio_button = "//tr[@aria-rowindex = 2]//td[1]"
action_button = "//span[contains(.,'Action')]"
stop_disabled_button = "//span[contains(.,'Stop') and @aria-disabled='true']"
delete_disabled_button = "//span[contains(.,'Delete') and @aria-disabled='true']"
action_delete_button = "//span[contains(.,'Delete')]"
action_stop_button = "//span[contains(.,'Stop')]"
pop_delete_button = "//button[@data-testid='delete-image-builder']"
refresh_button = "//button[@aria-label='Refresh data ']"
deleting = "//span[contains(.,'Deleting')]"
stopping = "//span[contains(.,'Stopping')]"
confirmation_of_iam_user = "//b[contains(.,'Account ID (12 digits)')]"
all_cookies = "//span[contains(., 'Accept all cookies')]"
dismiss = "//span[contains(., 'Dismiss')]"

# Fleet Locators
disassociate_fleet = "//span[contains(.,'Disassociate fleet')]"
confirm_disassociate = "//button[@data-testid='disassociate-fleet']/span[text()='Disassociate']"
application_button = "//span[contains(.,'Applications')]"
detail_button = "//span[contains(.,'Details')]"
edit_button = "//span[contains(.,'Edit')]"
associate_stack_get_text = "//div[contains(text(),'Associated Stack')]//following::div/a"
success_toast = "//div[text()='Success']"
fleet_time_created_header = "//th[7]/div"
fleet_detail_open_pop_up = "//h2[contains(text(),'Fleet name')]"
fleet_type_get_text = "//tr[@aria-rowindex = 2]//td[5]"
application_ratio_button = "//label[contains(@aria-label, 'Assigned application Selection Select')]/span"
disassociate_application = "//div[1]/button[@type='submit']/span[contains(.,'Disassociate')]"
disassociate_application_pop_up = "//div[2]/button[@type='submit']/span[contains(.,'Disassociate')]"
disassociate_application_toast = "//div[contains(text(),'Successfully disassociated application from fleet')]"
fleet_status_get_text = "//div[2]/span/span[contains(@class,'awsui_container_')]"
stop_button_pop_up = "//button/span[contains(.,'Stop')]"
fleet_pop_delete_button = "//button[@data-testid='delete-fleet-modal']/span"
fleet_detail_close_pop_up = "//div[contains(@class,'awsui_header-actions')]/button[@title='Close alert']/span"
