import string
import time
import random
from urllib.parse import urlparse

from behave import *
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.loginPage import LoginPage
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


@given("Access the React URL")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get(LoginPage.URL)
    context.driver.maximize_window()
    # implicit wait
    time.sleep(3)


@when("Click on Sign up option")
def step_impl(context):
    context.driver.find_element(By.XPATH, LoginPage.signUpBtn).click()


@step('Input username as "{username}" and email as "{email}" and Password as "{password}"')
def step_impl(context, username, email, password):
    # Maximum wait time of 10 seconds
    context.wait = WebDriverWait(context.driver, 10)
    # fluent wait
    context.wait.until(EC.visibility_of_element_located((By.XPATH, LoginPage.signUpScreen)))
    username = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(8, 8)))
    context.username = username
    email = username + "@gmail.com"
    context.driver.find_element(By.XPATH, LoginPage.Username).send_keys(username)
    context.driver.find_element(By.XPATH, LoginPage.Email).send_keys(email)
    context.driver.find_element(By.XPATH, LoginPage.Password).send_keys(password)


@step("Click on Sign up button")
def step_impl(context):
    context.driver.find_element(By.XPATH, LoginPage.SignUpInBtn).click()
    context.wait.until(EC.visibility_of_element_located((By.XPATH, LoginPage.SigninUsername + context.username + "']")))


@then("Home screen is display correctly with correct username")
def step_impl(context):
    context.driver.find_element(By.XPATH, LoginPage.SigninUsername + context.username + "']").is_displayed()
