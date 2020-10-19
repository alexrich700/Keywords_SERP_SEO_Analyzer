from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import csv
import requests
import word_counter
import writeCSV
from dotenv import load_dotenv

# Add search query
searchQuery = "marketing agency in victoria tx"
# Add path to download file relative to this script
pathToDownloadFile = r'../../Downloads'
# Add path to Chrome extension CRX file
ahrefExtension = r'C:\Users\alexr\AppData\Local\Programs\Python\Python39\Lib\site-packages\selenium\Extensions\ahrefs.crx'

# Load enviroment variables
load_dotenv()

# Get env variables
ahrefEmail = os.getenv("AHREF_EMAIL")
ahrefPassword = os.getenv("AHREF_PASSWORD")
PSI_API_Key = os.getenv("PSI_API_KEY")

# Add Ahrefs Chrome Extension
chrome_options = Options()
chrome_options.add_extension(ahrefExtension)

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=chrome_options)

# set implicit wait time 
driver.implicitly_wait(30) # seconds 

############################################################ AHREF Stuff ###########################################################

try: 

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

except:
    print("I hate life")

############################################################ Google Search Stuff ###########################################################

try: 
    # Open Google
    driver.get("https://google.com")

    # Preform a search
    search = driver.find_element_by_name("q")
    search.send_keys(searchQuery)
    search.send_keys(Keys.RETURN)

except:
    print('You suck at programming and should quit')

############################################################ Get Data ###########################################################

try: 

    # Sleep for 2s because without it the file won't download for some ungodly reason
    time.sleep(5)

    # Download CSV file
    ahrefCSV = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "__ah__toolbar__icon-csv"))
    ).click()

    # Sleep for 3s because without it the extension doesn't work for some ungodly reason
    time.sleep(2)

except:
    print("I'm quitting and becoming a musician")

try:
    ############################################################ CSV Stuff ###########################################################

    # Check if the latest file is finished downloading
    def latest_download_file():
        # Path to downloads file relative to this script
        path = r'../../Downloads'
        os.chdir(pathToDownloadFile)
        files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
        newest = files[-1]

        return newest
    
    # Save the filename once download is complete
    fileends = "crdownload"
    while "crdownload" == fileends:
        time.sleep(1)
        newest_file = latest_download_file()
        if "crdownload" in newest_file:
            fileends = "crdownload"
        else:
            fileends = "none"
            # Save the CSV to an array
            with open(newest_file, newline='') as csvfile:
                SERPData = list(csv.reader(csvfile))

    # Initiate array for result URLs
    serpURLs = []

    # Get the URLs from the array of SERP results
    for serp in SERPData:
        serpURLs.append(serp[2])

    # Remove header from URL data
    serpURLs.remove(serpURLs[0])
    # time.sleep(5)

except Exception as ex:
    print(ex)

try:
    ############################################################ Speed Stuff ###########################################################
    
    # Create arrays to store speed data
    speedIndex = ['Speed']
    largestPaint = ['Largest Contentful Paint']
    cumalativeLayoutShift = ['Cumalative Layout Shift']
    totalBlocking = ['Total Blocking Time']

    for i in serpURLs:
        # Call PSI API and save JSON 
        PSIRes = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=" + i + "&key=" + PSI_API_Key
        response = requests.get(PSIRes)
        speedRes = response.json()
        # Append speed data to arrays
        speedIndex.append(speedRes['lighthouseResult']['audits']['speed-index']['displayValue'])
        largestPaint.append(speedRes['lighthouseResult']['audits']['largest-contentful-paint']['displayValue'])
        cumalativeLayoutShift.append(speedRes['lighthouseResult']['audits']['cumulative-layout-shift']['displayValue'])
        totalBlocking.append(speedRes['lighthouseResult']['audits']['total-blocking-time']['displayValue'])

    # Add speed data to each row
    i = 0
    for row in SERPData:
        row.append(speedIndex[i])
        row.append(largestPaint[i])
        row.append(cumalativeLayoutShift[i])
        row.append(totalBlocking[i])
        i+=1

    # print(SERPData)
except: 
    print('Loser')

try:
    ############################################################ Word Counting Magic ###########################################################

    totalWordList = ['Word Count']
    topKeywordsList = ['Top 5 Words']

    for url in serpURLs:
        totalWords = word_counter.start(url)
        clean_list = word_counter.clean_wordlist(totalWords)
        topKeywords = word_counter.create_dictionary(clean_list)
        totalWordList.append(len(totalWords))
        topKeywordsList.append(topKeywords)

    i = 0
    for row in SERPData:
        row.append(totalWordList[i])
        row.append(topKeywordsList[i])
        i+=1

except: 
    print('Loser')

try:
    ############################################################ Write to CSV ###########################################################

    # Write the data to a CSV file
    writeCSV.write(SERPData, searchQuery)

except:
    print("Go back to JS")

finally:
    driver.quit()

