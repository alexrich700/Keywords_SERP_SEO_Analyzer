import requests
import os
from dotenv import load_dotenv

# Load enviroment variables
load_dotenv()

# Pagespeed Insights API Key
PSI_API_Key = os.getenv("PSI_API_KEY")

# Create arrays to store speed data
speedIndex = ['Speed']
largestPaint = ['Largest Contentful Paint']
cumalativeLayoutShift = ['Cumalative Layout Shift']
totalBlocking = ['Total Blocking Time']


def speedTest(serpURLs, SERPData):
    # Do speed tests
    pagespeedInsights(serpURLs)
    # Append the new data
    appendSpeedData(SERPData)

    return SERPData


def pagespeedInsights(serpURLs):
    i = 0
    for s in serpURLs:
        # Call PSI API and save JSON 
        PSIRes = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=" + s + "&key=" + PSI_API_Key
        response = requests.get(PSIRes)
        speedRes = response.json()
        print(i)
        print(len(serpURLs))
        print(s)
        print(serpURLs[i])
        # Append speed data to arrays
        speedIndex.append(speedRes['lighthouseResult']['audits']['speed-index']['displayValue'])
        largestPaint.append(speedRes['lighthouseResult']['audits']['largest-contentful-paint']['displayValue'])
        cumalativeLayoutShift.append(speedRes['lighthouseResult']['audits']['cumulative-layout-shift']['displayValue'])
        totalBlocking.append(speedRes['lighthouseResult']['audits']['total-blocking-time']['displayValue'])
        i+=1

def appendSpeedData(SERPData):
    i = 0
    print(speedIndex)
    print(len(speedIndex))
    print(SERPData)
    print(i)
    for row in SERPData:
        row.append(speedIndex[i])
        row.append(largestPaint[i])
        row.append(cumalativeLayoutShift[i])
        row.append(totalBlocking[i])
        i+=1
    # Clear the arrays for the next loop
    speedIndex.clear()
    largestPaint.clear()
    cumalativeLayoutShift.clear()
    totalBlocking.clear()
    return SERPData

