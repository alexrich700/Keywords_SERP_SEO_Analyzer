from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Import modules
import login_ahref
import google_search
import get_ahref_csv
import find_csv
import get_serp_data
import word_counter
import writeCSV
import speed_test

# Add search query
searchQuery = "contract analysis systems"

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

try:
    # AHREF Login
    login_ahref.loginAhref(driver)

    # Google Search Stuff 
    google_search.googleSearch(driver, searchQuery)

    # Get Ahref Data 
    get_ahref_csv.getAhrefData(driver)

    # CSV Stuff 
    newest = find_csv.latest_download_file()
    SERPData = get_serp_data.getCSV(newest)
    serpURLs = find_csv.get_URLs(SERPData)

    # Speed Stuff 
    SERPData = speed_test.speedTest(serpURLs, SERPData)

    # Word Counting Magic 
    SERPData = word_counter.wordCoutingMagic(serpURLs, SERPData)

    # Write to CSV 
    writeCSV.write(SERPData, searchQuery)

except Exception as ex:
    print(ex)

finally:
    driver.quit()