from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Import modules
from modules import login_ahref
from modules import google_search
from modules import get_ahref_csv
from modules import find_csv
from modules import get_serp_data
from modules import word_counter
from modules import writeCSV
from modules import speed_test

# Add search query
searchQueries = ["sterile compounding"]

# Add path to download file relative to this script
pathToDownloadFile = r'../../Downloads'
# Add path to Chrome extension CRX file
ahrefExtension = r'C:\Users\alexr\AppData\Local\Programs\Python\Python39\Lib\site-packages\selenium\Extensions\ahrefs.crx'

# Add Ahrefs Chrome Extension
chrome_options = Options()
chrome_options.add_extension(ahrefExtension)

# Add Chrome driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=chrome_options)

# AHREF Login
login_ahref.loginAhref(driver)

for searchQuery in searchQueries:

    # Google Search Stuff 
    google_search.googleSearch(driver, searchQuery)

    # Get Ahref Data 
    get_ahref_csv.getAhrefData(driver)

    # CSV Stuff 
    newest = find_csv.latest_download_file()
    print(newest)
    SERPData = get_serp_data.getCSV(newest)
    serpURLs = find_csv.get_URLs(SERPData)

    # Speed Stuff 
    SERPData = speed_test.speedTest(serpURLs, SERPData)

    # Word Counting Magic 
    SERPData = word_counter.wordCoutingMagic(serpURLs, SERPData)

    # Write to CSV 
    writeCSV.write(SERPData, searchQuery)

    # Clear the arrays for the next loop
    SERPData.clear()
    serpURLs.clear()

driver.quit()