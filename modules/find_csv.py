import os
import csv
import time


# Initiate array for result URLs
serpURLs = []

def get_URLs(SERPData):
    # Get the URLs from the array of SERP results
    for serp in SERPData:
        serpURLs.append(serp[2])

    # Remove header from URL data
    serpURLs.remove(serpURLs[0])

    return serpURLs

# Check if the latest file is finished downloading
def latest_download_file():
    # Path to downloads file relative to this script
    owd = os.getcwd()
    projectDirectory = r'C:\Users\alexr\Documents\Projects'
    # Check if the current working dir is the project's if not, change to downloads folder
    if owd == projectDirectory:
        path = r'../../Downloads'
        os.chdir(path)

    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    newest = files[-1]

    return newest

# Save the filename once download is complete
def save_File(newest):
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
    return SERPData
