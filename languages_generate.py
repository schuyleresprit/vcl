import os
import csv
import pandas as pd
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

# ----------
# Functions
# ----------

#-------------------------------------------------------------------------
# Returns a list of all the csv files in a directory
#-------------------------------------------------------------------------
def get_csv_list(csv_location):
  csv_list = []

  file_list = os.listdir(csv_location)
  for file in file_list:
    if file.lower().endswith('.csv'): csv_list.append(file)

  return csv_list
# -------------------------------------------------------------------------
# Returns a dictionary of author ids (key is the author name and the value is their id)
#-------------------------------------------------------------------------
def process_author_files(csv_path, csv_list):
  author_ids = {}
  publications_two = {}
  languages = {}
  english = {}
  french = {}
  spanish = {}
  dutch = {}
  portuguese = {}
  haitiancreole = {}
  italian = {}

  for csv_name in csv_list:
    with open(csv_path+csv_name) as csv_file:
      reader = csv.reader(csv_file)

#------------------------------------------------
# get the author information from the csv header based on language
#------------------------------------------------
      author_info = reader.__next__()

      if (not len(author_info) > 1) :
        print('This file does not have proper author info: ' + csv_name)
        print(author_info)
        break

      author_name = author_info[0]
      author_id = author_info[1]
      author_ids[author_name] = author_id
      languages[author_id] = []

#----------------------------------------------------------
#read the rest of each csv to get the author's publications
#----------------------------------------------------------
    for csv_name in csv_list:
        with open(csv_path+csv_name) as csv_file:
            reader = csv.DictReader(csv_file)
            row_index = 0
    
            for row in reader:    
            
                author_publications = {}
                author_publications['Author'] = author_info[0]
                author_publications['Title'] = row['Title']
                author_publications['Pubdate'] = row['Pubdate']
                author_publications['Language'] = row['Language']
                author_publications['Publisher'] = row['Publisher']
                author_publications['Genre'] = row['Genre']
                author_publications['Translation'] = row['Translation']
                author_publications['Descriptor'] =  row['Descriptor']

                publication_id = row['Title']
                author_publications['Title'] = publication_id
                language_id = row['Language']
                author_publications['Language'] = language_id
                genre_id = row['Genre']
                author_publications['Genre'] = genre_id
                translation_id = row['Translation']
                author_publications['Translation'] = translation_id
                date_id = row['Pubdate']
                author_publications['Pubdate'] = date_id

                publications_two[author_id].append(author_publications)
                row_index += 1
#-------------------------------------------------------------------------------
#Create a dictionary for the LANGUAGES, Genres, Timeline, Translations
#-------------------------------------------------------------------------------
    language_english = {}
    language_french = {}
    language_spanish = {}
    language_dutch = {}
    language_portuguese = {}
    language_haitiancreole = {}
    language_italian = {}

    for csv_name in csv_list:
        with open(csv_path+csv_name) as csv_file:
            reader = csv.reader(csv_file)
        for i in range(2):

            if not row['Language'] in languages:
                languages[row['Language']] = ['English']
            if not row['Language'] in language_english:
                language_english[row['Language']] = []
                languages[language_id].append(languages)
                row_index += 1
#-------------------------------------------------------------------------------
        for i in range(2):
           if not row['Language'] in languages:
            languages[row['Language']] = ['French']
        if not row['Language'] in language_french:
            language_french[row['Language']] = []
            languages[language_id].append(languages)
            row_index += 1
#-------------------------------------------------------------------------------
        for i in range(2):
           if not row['Language'] in languages:
            languages[row['Language']] = ['Spanish']
        if not row['Language'] in language_spanish:
            language_spanish[row['Language']] = []
            languages[language_id].append(languages)
            row_index += 1
#-------------------------------------------------------------------------------
        for i in range(2):
           if not row['Language'] in languages:
            languages[row['Language']] = ['Dutch']
        if not row['Language'] in language_dutch:
            language_dutch[row['Language']] = []
            languages[language_id].append(languages)
            row_index += 1
#-------------------------------------------------------------------------------
        for i in range(2):
           if not row['Language'] in languages:
            languages[row['Language']] = ['Portuguese']
        if not row['Language'] in language_portuguese:
            language_portuguese[row['Language']] = []
            languages[language_id].append(languages)
            row_index += 1
#-------------------------------------------------------------------------------
        for i in range(2):
           if not row['Language'] in languages:
            languages[row['Language']] = ['Haitian Creole']
        if not row['Language'] in language_haitiancreole:
            language_haitiancreole[row['Language']] = []
            languages[language_id].append(languages)
            row_index += 1
#-------------------------------------------------------------------------------
        for i in range(2):
           if not row['Language'] in languages:
            languages[row['Language']] = ['Italian']
        if not row['Language'] in language_italian:
            language_italian[row['Language']] = []
            languages[language_id].append(languages)
            row_index += 1
   
    csv_file.close()
 
 
    return language_english, language_french, language_spanish, language_dutch, language_portuguese, language_haitiancreole, language_italian

# ---------------
# Function calls
# ---------------
csv_list = get_csv_list(CSV_LOCATION)
language_english, language_french, language_spanish, language_dutch, language_portuguese, language_haitiancreole, language_italian = process_author_files(CSV_LOCATION, csv_list)


with codecs.open(ENGLISH_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(language_english, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(FRENCH_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(language_french, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(SPANISH_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(language_spanish, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(DUTCH_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(language_dutch, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(PORTUGUESE_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(language_portuguese, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(HAITIANCREOLE_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(language_haitiancreole, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(ITALIAN_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(language_italian, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()


          