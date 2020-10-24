# from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# Gets the CSV from Ahref
def getAhrefData(driver):
    time.sleep(5)
    # Download CSV file
    ahrefCSV = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "__ah__toolbar__icon-csv"))
    ).click()

    time.sleep(2)