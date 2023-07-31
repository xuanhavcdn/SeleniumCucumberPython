import string
import time
import random
import json
from behave import *
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.SignInPage import SignInPage
from pages.signUpPage import SignupPage
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


@when("Click on Sign in option button")
def step_impl(context):
    context.driver.find_element(By.XPATH, SignInPage.signInBtn).click()
    context.wait = WebDriverWait(context.driver, 10)

@step('Input email as "{email}" and password as "{password}"')
def step_impl(context, email, password):
    with open('user_data.json', 'r') as json_file:
        data = json.load(json_file)
    email = data['email']
    context.email = email
    context.driver.find_element(By.XPATH, SignupPage.Email).send_keys(email)
    context.driver.find_element(By.XPATH, SignupPage.Password).send_keys(password)
