import csv

def write (serpDATA, searchQuery):
    arr = serpDATA

    f = open(searchQuery + ".csv", "w", newline="")

    writer = csv.writer(f)

    for row in arr:
        writer.writerow(row)

    f.close()