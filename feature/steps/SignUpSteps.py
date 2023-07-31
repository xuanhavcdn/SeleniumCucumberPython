import string
import time
import random
import json
from behave import *
from selenium.webdriver import Keys
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.signUpPage import SignupPage
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


@given("Access the React URL")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get(SignupPage.URL)
    context.driver.maximize_window()
    # implicit wait
    time.sleep(3)
    context.wait = WebDriverWait(context.driver, 10)


@when("Click on Sign up option")
def step_impl(context):
    context.driver.find_element(By.XPATH, SignupPage.signUpBtn).click()


@step('Input username as "{username}" and email as "{email}" and Password as "{password}"')
def step_impl(context, username, email, password):
    # fluent wait
    context.wait.until(EC.visibility_of_element_located((By.XPATH, SignupPage.signUpScreen)))
    username = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(8, 8)))
    context.username = username
    email = username + "@gmail.com"
    context.driver.find_element(By.XPATH, SignupPage.Username).send_keys(username)
    context.driver.find_element(By.XPATH, SignupPage.Email).send_keys(email)
    context.driver.find_element(By.XPATH, SignupPage.Password).send_keys(password)
    # Write email and username data to JSON file
    data = {
        "email": email,
        "username": username
    }
    json_file_path = "feature/test_data/user_data.json"  # Change the file path as needed
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file)


@step("Click on Sign up button")
def step_impl(context):
    context.driver.find_element(By.XPATH, SignupPage.SignUpInBtn).click()


@then("Home screen is displayed correctly with correct username")
def step_impl(context):
    with open('feature/test_data/user_data.json', 'r') as json_file:
        data = json.load(json_file)
    username = data['username']
    context.wait.until(EC.visibility_of_element_located((By.XPATH, SignupPage.SigninUsername + username + "']")))
