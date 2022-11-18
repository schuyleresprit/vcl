import os
import csv
import pandas as pd
import datetime
import codecs
import json
from geopy import geocoders
from operator import itemgetter

# ---------
# Settings
# ---------

CSV_LOCATION = os.getcwd() + '/raw-data/'
ENGLISH_JSON = os.getcwd() + 'data/english.json'
FRENCH_JSON = os.getcwd() + 'data/french.json'
SPANISH_JSON = os.getcwd() + 'data/spanish.json'
DUTCH_JSON = os.getcwd() + 'data/dutch.json'
PORTUGUESE_JSON = os.getcwd() + 'data/portuguese.json'
HAITIANCREOLE_JSON = os.getcwd() + 'data/haitiancreole.json'
ITALIAN_JSON = os.getcwd() + 'data/italian.json'


 with open(csv_path+csv_name) as csv_file:
          reader = csv.reader(csv_file)
        for i in range(2):

          if not row['Language'] in languages:
            languages[row['Language']] = []
          if not row['Language'] in publications_by_language:
            publications_by_language[row['Language']] = []
            languages[language_id].append(author_publications)
            row_index += 1