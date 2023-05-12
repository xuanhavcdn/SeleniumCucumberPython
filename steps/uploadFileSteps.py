import time
from behave import *
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.uploadFilePage import TestUpload
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


@given("Access the URL")
def step_impl(context):
    context.driver = webdriver.Chrome("/Users/ha.cao/Desktop/Python_Selenium_Cucumber/chromedriver.exe")
    context.driver.get(TestUpload.URL)
    context.driver.maximize_window()


@when("Submit the file")
def step_impl(context):
    upload_btn = context.driver.find_element(By.XPATH, TestUpload.UploadFileBtn)
    upload_btn.send_keys("/Users/ha.cao/Desktop/driver/chromedriver_mac_arm64.zip")


@then("Close browser")
def step_impl(context):
    context.driver.quit()


@step("Click on Submit button")
def step_impl(context):
    context.driver.find_element(By.XPATH, TestUpload.SubmitBtn).click()


@then('The "{message}" message is displayed correctly')
def step_impl(context, message):
    # time.sleep(5)
    # context.driver.find_element(By.CSS_SELECTOR, TestUpload.SuccessMessageCss)
    wait = WebDriverWait(context.driver, 1)
    if message == "success":
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, TestUpload.SuccessMessageCss)))
    else:
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, TestUpload.ErrorMessageCss)))


@step('"{Ticked_status}" check box accept term of service')
def step_impl(context, Ticked_status):
    if Ticked_status == "Yes":
        context.driver.find_element(By.XPATH, TestUpload.CheckBoxTermOfService).click()


@when('Submit the file "{file_storage}" MB')
def step_impl(context, file_storage):
    upload_btn = context.driver.find_element(By.XPATH, TestUpload.UploadFileBtn)
    if float(file_storage) == 196.45:
        upload_btn.send_keys("/Users/ha.cao/Desktop/driver/chromedriver_mac_arm64.zip")
    elif float(file_storage) == 196.44:
        upload_btn.send_keys("/Users/ha.cao/Desktop/driver/chromedriver_mac_arm64.zip")
    elif float(file_storage) == 196.46:
        upload_btn.send_keys("/Users/ha.cao/Desktop/driver/chromedriver_mac_arm64.zip")

@when("Click on Term of Service link")
def step_impl(context):
    context.driver.find_element(By.XPATH, TestUpload.TermOfServiceURL).click()


@then("The Term of Service link is displayed correctly")
def step_impl(context):
    context.driver.switch_to.window(context.driver.window_handles[-1])
    time.sleep(10)
    actualUrl = context.driver.current_url
    assert actualUrl == TestUpload.TermOfServicePage
