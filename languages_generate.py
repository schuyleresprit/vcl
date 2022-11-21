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
      languages = reader.__next__()

      if (not len(author_info) > 1) :
        print('This file does not have proper author info: ' + csv_name)
        print(author_info)
        break

      author_name = author_info[0]
      author_id = author_info[1]
      author_country = author_info[2]
      author_ids[author_name] = author_id
      languages[author_id] = []

#----------------------------------------------------------
#read the rest of each csv to get the author's publications
#----------------------------------------------------------
    languages = {}
    languages['Author'] = author_info[0]
    languages['Title'] = row['Title']
    languages['Pubdate'] = row['Pubdate']
    languages['Language'] = row['Language']
    languages['Publisher'] = row['Publisher']
    languages['Genre'] = row['Genre']
    languages['Translation'] = row['Translation']
    languages['Descriptor'] =  row['Descriptor']

    publication_id = row['Title']
    languages['Title'] = publication_id
    language_id = row['Language']
    languages['Language'] = language_id
    genre_id = row['Genre']
    languages['Genre'] = genre_id
    translation_id = row['Translation']
    languages['Translation'] = translation_id
    date_id = row['Pubdate']
    languages['Pubdate'] = date_id

    languages[author_id].append(publications)
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
    with open(csv_path+csv_name) as csv_file:
          reader = csv.reader(csv_file)
    for i in range(2):

          if not row['Language'] in languages:
            languages[row['Language']] = []
          if not row['Language'] in publications_by_language:
            publications_by_language[row['Language']] = []
            languages[language_id].append(languages)
            row_index += 1