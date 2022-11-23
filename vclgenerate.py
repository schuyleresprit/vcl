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

CSV_LOCATION = os.getcwd() + '/raw-data-2/'
AUTHOR_ID_JSON = os.getcwd() + '/data/author_ids.json'
TIMELINE_JSON = os.getcwd() + '/data/timeline.json'
INTERSECTIONS_JSON = os.getcwd() + '/data/intersections.json'
PLACES_JSON = os.getcwd() + '/data/places.json'
COUNTRIES_JSON = os.getcwd() + '/data/countries.json'
LANGUAGES_JSON = os.getcwd() + '/data/languages.json'
GENRES_JSON = os.getcwd() + '/data/genres.json'
TRANSLATIONS_JSON = os.getcwd() + '/data/translations.json'
PUBLICATIONS_JSON = os.getcwd() + '/data/publications.json'
GEONAMES_USERNAME = 'schuylere'

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

#-------------------------------------------------------------------------
# Returns the GeoNames latitude and longitude of the place name provided.
# If the place is not found, the function returns None for both longitude and latitude.
#-------------------------------------------------------------------------
def get_lat_long(place_name, geonames_username):
  gn = geocoders.GeoNames(username=geonames_username, timeout=None)
  location = gn.geocode(place_name,timeout=None)
  if location == None:
    print(place_name, "not found.")
    return None, None
  else:
    return location.latitude, location.longitude
#--------------------------------------------------------------------------
def get_author_country_geo(author_country, geonames_username):
  gn = geocoders.GeoNames(username=geonames_username, timeout=None)
  location = gn.geocode(author_country,timeout=None)
  if location == None:
    print(author_country, "not found.")
    return None, None
  else:
    return location.latitude, location.longitude
# -------------------------------------------------------------------------
# Returns a dictionary of author ids (key is the author name and the value is their id)
# Returns a dictionary of places
# places = { 'PlaceName': {'Lat': xxx, 'Long': yyy, 'Pub_id': ##}, ... }
# Returns a dictionary each author movement# The keys for each movement in the author_movements dictionary are as follows:
#-------------------------------------------------------------------------
def process_author_files(csv_path, csv_list, geonames_username):
  author_ids = {}
  publications = {}
  places = {}
  countries = {}
  languages = {}
  genres = {}
  timeline = {}
  translations = {}

  for csv_name in csv_list:
    with open(csv_path+csv_name) as csv_file:
      reader = csv.reader(csv_file)

#------------------------------------------------
# get the author information from the csv header
#------------------------------------------------
      author_info = reader.__next__()

      if (not len(author_info) > 1) :
        print('This file does not have proper author info: ' + csv_name)
        print(author_info)
        break

      author_name = author_info[0]
      author_id = author_info[1]
      author_country = author_info[2]
      author_ids[author_name] = author_id
      publications[author_id] = []

#----------------------------------------------------------------
#get author country coordinates for each author_id
#----------------------------------------------------------------
      lat, long = get_author_country_geo(author_country, geonames_username)

      country_name = author_info[2]
      if not country_name in countries:
        country_info = {}
        country_info['Lat'] = lat
        country_info['Long'] = long
        country_id = author_info[2]
        country_info['author_country'] = country_id
        countries[country_name] = country_info

#-------------------------------------------------------------------
#get Pub_id coordinates for each Pub_id
#-------------------------------------------------------------------
      reader = csv.DictReader(csv_file)
      row_index = 0
      for row in reader:
        #Skip improperly formated file
        if ((not 'City' in row) or (not 'Country' in row)) :
          print('The file ' + csv_name + ' are missing the keys to create place name!')
          break

        if not(row['Title'] == '' and row['Pubdate'] == '' and row['Language'] == '' and row['Genre'] == ''):
          place_name = row['City'] + ', ' + row['Country']

        if not place_name in places:
          place_info = {}

          lat, long = get_lat_long(place_name, geonames_username)
          place_info['Lat'] = lat
          place_info['Long'] = long

          place_id = row['Pub_id']
          place_info['Pub_id'] = place_id

          places[place_name] = place_info

#----------------------------------------------------------
#read the rest of each csv to get the author's publications
#----------------------------------------------------------
        author_publications = {}
        author_publications['Author'] = author_info[0]
        author_publications['Pub_id'] = places[place_name]['Pub_id']
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

        publications[author_id].append(author_publications)
        row_index += 1
#-------------------------------------------------------------------------------
#Create a dictionary for the LANGUAGES, Genres, Timeline, Translations
#-------------------------------------------------------------------------------
        publications_by_language = {}
        publications_by_genre = {}
        publications_by_timeline = {}
        publications_by_translation = {}

        with open(csv_path+csv_name) as csv_file:
          reader = csv.reader(csv_file)
        for i in range(2):

          if not row['Language'] in languages:
            languages[row['Language']] = []
          if not row['Language'] in publications_by_language:
            publications_by_language[row['Language']] = []
            languages[language_id].append(author_publications)
            row_index += 1
#-------------------------------------------------------------------------------
        for i in range(2):
          if not row['Genre'] in genres:
            genres[row['Genre']] = []
          if not row['Genre'] in publications_by_genre:
            publications_by_genre[row['Genre']] = []
            genres[genre_id].append(author_publications)
            row_index += 1
#-------------------------------------------------------------------------------
        for i in range(2):
          if not row['Pubdate'] in timeline:
            timeline[row['Pubdate']] = []
          if not row['Pubdate'] in publications_by_timeline:
            publications_by_timeline[row['Pubdate']] = []
            timeline[date_id].append(author_publications)
            row_index += 1
            #print(author_publications)
        for i in range (2):
          #print(author_publications)
          #if not row['Translation'] in translations:
          #	translations[row['Translation']] = []
          if not row['Translation'] in publications_by_translation:
            publications_by_translation[row['Translation']] = []
            if translation_id == 'y':
              #translations[translation_id].append(author_publications)
              translations.setdefault(translation_id, []).append(author_publications)
            row_index =+ 1

  csv_file.close()

  return author_ids, publications, places, countries, languages, genres, timeline, translations


# ---------------
# Function calls
# ---------------
csv_list = get_csv_list(CSV_LOCATION)
author_ids, publications, places, countries, languages, genres, timeline, translations = process_author_files(CSV_LOCATION, csv_list, GEONAMES_USERNAME)

with codecs.open(AUTHOR_ID_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(author_ids, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(COUNTRIES_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(countries, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(PLACES_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(places, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(LANGUAGES_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(languages, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(GENRES_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(genres, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(TIMELINE_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(timeline, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(PUBLICATIONS_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(publications, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(TRANSLATIONS_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(translations, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()
