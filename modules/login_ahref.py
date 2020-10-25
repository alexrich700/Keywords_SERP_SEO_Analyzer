from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
import time

# Load enviroment variables
load_dotenv()

# Get env variables
ahrefEmail = os.getenv("AHREF_EMAIL")
ahrefPassword = os.getenv("AHREF_PASSWORD")

def loginAhref(driver):
    driver.get("https://ahrefs.com/user/login")

    loginForm = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "form"))
    )

    # Grab form inputs
    emailInput = loginForm.find_element_by_name("email")
    passwordInput = loginForm.find_element_by_name("password")

    # Input Username and Password then login
    emailInput.send_keys(ahrefEmail)
    passwordInput.send_keys(ahrefPassword)
    passwordInput.send_keys(Keys.RETURN)

    # Sleep for 1s because without it the extension doesn't login for some ungodly reason
    time.sleep(1)