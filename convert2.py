import csv
import json

# defining the function to convert CSV file to JSON file
def convjson(csvFilename, jsonFilename):

    # creating a dictionary
    mydata = {}

    # reading the data from CSV file
    with open(csvFilename) as csvfile:
        csvRead = csv.DictReader(csvfile)

        # Converting rows into dictionary and adding it to data
        for rows in csvRead:

            mykey = rows['Author']
            mydata[mykey] = rows

    # dumping the data
    with open(jsonFilename, 'w') as jsonfile:
        jsonfile.write(json.dumps(mydata, ensure_ascii=False, indent = 4))

# filenames
csvFilename = r'language.csv'
jsonFilename = r'language.json'

# Calling the convjson function
convjson(csvFilename, jsonFilename)
