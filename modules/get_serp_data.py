import time
import csv

# Gets the latest downloaded CSV
def getCSV(newest):
    fileends = "crdownload"
    while "crdownload" == fileends:
        time.sleep(1)
        newest_file = newest
        print(newest_file)
        if "crdownload" in newest_file:
            fileends = "crdownload"
        else:
            fileends = "none"
            # Save the CSV to an array
            with open(newest_file, newline='') as csvfile:
                SERPData = list(csv.reader(csvfile))

    return SERPData