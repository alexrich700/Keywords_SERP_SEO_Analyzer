import requests
import os
from dotenv import load_dotenv

# Load enviroment variables
load_dotenv()

# Pagespeed Insights API Key
PSI_API_Key = os.getenv("PSI_API_KEY")

# Create arrays to store speed data
speedIndex = []
largestPaint = []
cumalativeLayoutShift = []
totalBlocking = []

def speedTest(serpURLs, SERPData):
    # Do speed tests
    pagespeedInsights(serpURLs)
    # Append the new data
    appendSpeedData(SERPData)

    return SERPData


def pagespeedInsights(serpURLs):
    # Create arrays to store speed data
    speedIndex.append('Speed')
    largestPaint.append('Largest Contentful Paint')
    cumalativeLayoutShift.append('Cumalative Layout Shift')
    totalBlocking.append('Total Blocking Time')

    for s in serpURLs:
        # Call PSI API and save JSON 
        PSIRes = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=" + s + "&key=" + PSI_API_Key
        response = requests.get(PSIRes)
        speedRes = response.json()
        # Append speed data to arrays
        speedIndex.append(speedRes['lighthouseResult']['audits']['speed-index']['displayValue'])
        largestPaint.append(speedRes['lighthouseResult']['audits']['largest-contentful-paint']['displayValue'])
        cumalativeLayoutShift.append(speedRes['lighthouseResult']['audits']['cumulative-layout-shift']['displayValue'])
        totalBlocking.append(speedRes['lighthouseResult']['audits']['total-blocking-time']['displayValue'])

def appendSpeedData(SERPData):
    i = 0
    for r in SERPData:
        print(r)
        r.append(speedIndex[i])
        r.append(largestPaint[i])
        r.append(cumalativeLayoutShift[i])
        r.append(totalBlocking[i])
        i+=1
    # Clear the arrays for the next loop
    speedIndex.clear()
    largestPaint.clear()
    cumalativeLayoutShift.clear()
    totalBlocking.clear()
    return SERPData

