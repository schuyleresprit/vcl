import os
import csv
import pandas as pd
#import datetime
import codecs
import json
import geocoder
from mapbox import Geocoder
from geopy import geocoders
from operator import itemgetter

# ---------
# Settings
# ---------

CSV_LOCATION = os.getcwd() + '/raw-data/'
AUTHOR_ID_JSON = os.getcwd() + '/data/author_ids.json'
TIMELINE_JSON = os.getcwd() + '/data/timeline.json'
INTERSECTIONS_JSON = os.getcwd() + '/data/intersections.json'
PLACES_JSON = os.getcwd() + '/data/places.json'
COUNTRIES_JSON = os.getcwd() + '/data/countries.json'
LANGUAGES_JSON = os.getcwd() + '/data/languages.json'
GENRES_JSON = os.getcwd() + '/data/genres.json'
TRANSLATIONS_JSON = os.getcwd() + '/data/translations.json'
PUBLICATIONS_JSON = os.getcwd() + '/data/publications.json'
ENGLISH_JSON = os.getcwd() + '/data/english.json'
FRENCH_JSON = os.getcwd() + '/data/french.json'
SPANISH_JSON = os.getcwd() + '/data/spanish.json'
DUTCH_JSON = os.getcwd() + '/data/dutch.json'
PORTUGUESE_JSON = os.getcwd() + '/data/portuguese.json'
HAITIANCREOLE_JSON = os.getcwd() + '/data/haitiancreole.json'
ITALIAN_JSON = os.getcwd() + '/data/italian.json'
ARABIC_JSON = os.getcwd() + '/data/arabic.json'
CHINESE_JSON = os.getcwd() + '/data/chinese.json'
CREOLE_JSON = os.getcwd() + '/data/creole.json'
CZECH_JSON = os.getcwd() + '/data/czech.json'
DANISH_JSON = os.getcwd() + '/data/danish.json'
ESTONIAN_JSON = os.getcwd() + '/data/estonian.json'
FINNISH_JSON = os.getcwd() + '/data/finnish.json'
FRENCHCREOLE_JSON = os.getcwd() + '/data/frenchcreole.json'
GERMAN_JSON = os.getcwd() + '/data/german.json'
GREEK_JSON = os.getcwd() + '/data/greek.json'
GREEKMODERN_JSON = os.getcwd() + '/data/greekmodern.json'
HEBREW_JSON = os.getcwd() + '/data/hebrew.json'
HUNGARIAN_JSON = os.getcwd() + '/data/hungarian.json'
JAPANESE_JSON = os.getcwd() + '/data/japanese.json'
KOREAN_JSON = os.getcwd() + '/data/korean.json'
LATVIAN_JSON = os.getcwd() + '/data/latvian.json'
NORWEGIAN_JSON = os.getcwd() + '/data/norwegian.json'
PERSIAN_JSON = os.getcwd() + '/data/persian.json'
FARSI_JSON = os.getcwd() + '/data/farsi.json'
POLISH_JSON = os.getcwd() + '/data/polish.json'
ROMANIAN_JSON = os.getcwd() + '/data/romanian.json'
RUSSIAN_JSON = os.getcwd() + '/data/russian.json'
SERBIAN_JSON = os.getcwd() + '/data/serbian.json'
SLOVENIAN_JSON = os.getcwd() + '/data/slovenian.json'
SPANISHFRENCH_JSON = os.getcwd() + '/data/spanishfrench.json'
SLUCREOLE_JSON = os.getcwd() + '/data/slucreole.json'
SWEDISH_JSON = os.getcwd() + '/data/swedish.json'
TURKISH_JSON = os.getcwd() + '/data/turkish.json'
VIETNAMESE_JSON = os.getcwd() + '/data/vietnamese.json'
WELSH_JSON = os.getcwd() + '/data/welsh.json'
FICTIONNOVEL_JSON = os.getcwd() + '/data/fictionnovel.json'
FICTIONSTORY_JSON = os.getcwd() + '/data/fictionstory.json'
FICTIONSTORYCOLL_JSON = os.getcwd() + '/data/fictionstorycoll.json'
POEM_JSON = os.getcwd() + '/data/poem.json'
POETRYCOLL_JSON = os.getcwd() + '/data/poetrycoll.json'
DRAMA_JSON = os.getcwd() + '/data/drama.json'
MEMOIR_JSON = os.getcwd() + '/data/memoir.json'
ANTHOLOGY_JSON = os.getcwd() + '/data/anthology.json'
NONFICTION_JSON = os.getcwd() + '/data/nonfiction.json'
ESSAY_JSON = os.getcwd() + '/data/essay.json'
MAPBOX_USERNAME = 'schuylere'
access_token = 'pk.eyJ1Ijoic2NodXlsZXJlIiwiYSI6ImNsMmh3aGRuMjAxN3MzaW1rMmZoenhpMTMifQ.Nwv-MP6OK6eOKW_bfNYRaw'
#GEONAMES_USERNAME = 'schuylere'

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
def get_lat_long(place_name, mapbox_username):
  location = geocoder.mapbox(place_name, username=mapbox_username, timeout=None)
  if location == None:
    print(place_name, "not found.")
    return None, None
  else:
    return location.lat, location.lng
#--------------------------------------------------------------------------
def get_author_country_geo(author_country, mapbox_username):
  location = geocoder.mapbox(author_country, username=mapbox_username, timeout=None)
  if location == None:
    print(author_country, "not found.")
    return None, None
  else:
    return location.lat, location.lng
# -------------------------------------------------------------------------
# Returns a dictionary of author ids (key is the author name and the value is their id)
# Returns a dictionary of places
# places = { 'PlaceName': {'Lat': xxx, 'Long': yyy, 'Pub_id': ##}, ... }
# Returns a dictionary each author movement# The keys for each movement in the author_movements dictionary are as follows:
#-------------------------------------------------------------------------
def process_author_files(csv_path, csv_list, mapbox_username):
  author_ids = {}
  publications = {}
  places = {}
  countries = {}
  languages = {}
  genres = {}
  timeline = {}
  translations = {}
  english = {}
  french = {}
  spanish = {}
  dutch = {}
  portuguese = {}
  haitiancreole = {}
  italian = {}
  arabic = {}
  chinese = {}
  creole = {}
  czech = {}
  danish = {}
  estonian = {}
  finnish = {}
  frenchcreole = {}
  german = {}
  greek = {}
  greekmodern = {}
  hebrew = {}
  hungarian = {}
  japanese = {}
  korean = {}
  latvian = {}
  norwegian = {}
  persian = {}
  farsi = {}
  polish = {}
  romanian = {}
  russian = {}
  serbian = {}
  slovenian = {}
  spanishfrench = {}
  slucreole = {}
  swedish = {}
  turkish = {}
  vietnamese = {}
  welsh = {}
  fictionnovel = {}
  fictionstory = {}
  fictionstorycoll = {}
  poem = {}
  poetrycoll = {}
  drama = {}
  memoir = {}
  anthology = {}
  nonfiction = {}
  essay = {}
 
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
      lat, long = get_author_country_geo(author_country, mapbox_username)

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
        #print(row)
        
        #Skip improperly formated file
        if ((not 'City' in row) or (not 'Country' in row)) :
          print('The file ' + csv_name + ' are missing the keys to create place name!')
          break

        if not(row['Title'] == '' and row['Pubdate'] == '' and row['Language'] == '' and row['Genre'] == ''):
          place_name = row['Pub_id']
          #row['City'] + ', ' + row['Country']
        #print(author_id)
        if not place_name in places:
          place_info = {}

          lat, long = get_lat_long(place_name, mapbox_username)
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
        author_publications['Descriptor'] = row['Descriptor']

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
#-------------------------------------------------------------------------------
        for i in range (2):
          if not row['Translation'] in publications_by_translation:
            publications_by_translation[row['Translation']] = []
            if translation_id == 'y':
              translations.setdefault(translation_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['English']:
            publications_by_language[row['Language']] = []
            if language_id == 'English':
              english.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['French']:
            publications_by_language[row['Language']] = []
            if language_id == 'French':
              french.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Spanish']:
            publications_by_language[row['Language']] = []
            if language_id == 'Spanish':
              spanish.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Dutch']:
            publications_by_language[row['Language']] = []
            if language_id == 'Dutch':
              dutch.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Portuguese']:
            publications_by_language[row['Language']] = []
            if language_id == 'Portuguese':
              portuguese.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Haitian Creole']:
            publications_by_language[row['Language']] = []
            if language_id == 'Haitian Creole':
              haitiancreole.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Italian']:
            publications_by_language[row['Language']] = []
            if language_id == 'Italian':
              italian.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Arabic']:
            publications_by_language[row['Language']] = []
            if language_id == 'Arabic':
              arabic.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Chinese']:
            publications_by_language[row['Language']] = []
            if language_id == 'Chinese':
              chinese.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Creole']:
            publications_by_language[row['Language']] = []
            if language_id == 'Creole':
              creole.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Czech']:
            publications_by_language[row['Language']] = []
            if language_id == 'Czech':
              czech.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Danish']:
            publications_by_language[row['Language']] = []
            if language_id == 'Danish':
              arabic.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Estonian']:
            publications_by_language[row['Language']] = []
            if language_id == 'Estonian':
              estonian.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Finnish']:
            publications_by_language[row['Language']] = []
            if language_id == 'Finnish':
              finnish.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['French Creole']:
            publications_by_language[row['Language']] = []
            if language_id == 'French Creole':
              frenchcreole.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['German']:
            publications_by_language[row['Language']] = []
            if language_id == 'German':
              german.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Greek']:
            publications_by_language[row['Language']] = []
            if language_id == 'Greek':
              greek.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Greek, Modern']:
            publications_by_language[row['Language']] = []
            if language_id == 'Greek, Modern':
              greekmodern.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Hebrew']:
            publications_by_language[row['Language']] = []
            if language_id == 'Hebrew':
              hebrew.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Hungarian']:
            publications_by_language[row['Language']] = []
            if language_id == 'Hungarian':
              hungarian.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Japanese']:
            publications_by_language[row['Language']] = []
            if language_id == 'Japanese':
              japanese.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Korean']:
            publications_by_language[row['Language']] = []
            if language_id == 'Korean':
              korean.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Latvian']:
            publications_by_language[row['Language']] = []
            if language_id == 'Latvian':
              latvian.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Norwegian']:
            publications_by_language[row['Language']] = []
            if language_id == 'Norwegian':
              norwegian.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Persian']:
            publications_by_language[row['Language']] = []
            if language_id == 'Persian':
              persian.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Persian (Farsi)']:
            publications_by_language[row['Language']] = []
            if language_id == 'Persian (Farsi)':
              farsi.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Polish']:
            publications_by_language[row['Language']] = []
            if language_id == 'Polish':
              polish.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Romanian']:
            publications_by_language[row['Language']] = []
            if language_id == 'Romanian':
              romanian.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Russian']:
            publications_by_language[row['Language']] = []
            if language_id == 'Russian':
              russian.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Serbian']:
            publications_by_language[row['Language']] = []
            if language_id == 'Serbian':
              serbian.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Slovenian']:
            publications_by_language[row['Language']] = []
            if language_id == 'Slovenian':
              slovenian.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Spanish & French']:
            publications_by_language[row['Language']] = []
            if language_id == 'Spanish & French':
              spanishfrench.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['St. Lucian French Creole']:
            publications_by_language[row['Language']] = []
            if language_id == 'St. Lucian French Creole':
              slucreole.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Swedish']:
            publications_by_language[row['Language']] = []
            if language_id == 'Swedish':
              swedish.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Turkish']:
            publications_by_language[row['Language']] = []
            if language_id == 'Turkish':
              turkish.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Vietnamese']:
            publications_by_language[row['Language']] = []
            if language_id == 'Vietnamese':
              vietnamese.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Language'] in publications_by_language == ['Welsh']:
            publications_by_language[row['Language']] = []
            if language_id == 'Welsh':
              welsh.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Genre'] in publications_by_genre == ['Fiction (Novel)']:
            publications_by_genre[row['Genre']] = []
            if genre_id == 'Fiction (Novel)':
              fictionnovel.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Genre'] in publications_by_genre == ['Fiction (Short Story)']:
            publications_by_genre[row['Genre']] = []
            if genre_id == 'Fiction (Short Story)':
              fictionstory.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Genre'] in publications_by_genre == ['Fiction (Short Story Collection)']:
            publications_by_genre[row['Genre']] = []
            if genre_id == 'Fiction (Short Story Collection)':
              fictionstorycoll.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Genre'] in publications_by_genre == ['Poem']:
            publications_by_genre[row['Genre']] = []
            if genre_id == 'Poem':
              poem.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Genre'] in publications_by_genre == ['Poetry Collection']:
            publications_by_genre[row['Genre']] = []
            if genre_id == 'Poetry Collection':
              poetrycoll.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Genre'] in publications_by_genre == ['Drama']:
            publications_by_genre[row['Genre']] = []
            if genre_id == 'Drama':
              drama.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Genre'] in publications_by_genre == ['Autobiogaphy/ Memoir']:
            publications_by_genre[row['Genre']] = []
            if genre_id == 'Autobiography/ Memoir':
              memoir.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Genre'] in publications_by_genre == ['Anthology']:
            publications_by_genre[row['Genre']] = []
            if genre_id == 'Anthology':
              anthology.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Genre'] in publications_by_genre == ['Nonfiction']:
            publications_by_genre[row['Genre']] = []
            if genre_id == 'Nonfiction':
              nonfiction.setdefault(author_id, []).append(author_publications)
            row_index =+ 1
#-------------------------------------------------------------------------------       
        for i in range (2):
          if not row['Genre'] in publications_by_genre == ['Essay']:
            publications_by_genre[row['Genre']] = []
            if genre_id == 'Essay':
              essay.setdefault(author_id, []).append(author_publications)
            row_index =+ 1

  csv_file.close()

  return author_ids, publications, places, countries, languages, genres, timeline, translations, english, french, spanish, dutch, portuguese, haitiancreole, italian, arabic, chinese, creole, czech, danish, estonian, finnish, frenchcreole, german, greek, greekmodern, hebrew, hungarian, japanese, korean, latvian, norwegian, persian, farsi, polish, romanian, russian, serbian, slovenian, spanishfrench, slucreole, swedish, turkish, vietnamese, welsh, fictionnovel, fictionstory, fictionstorycoll, poem, poetrycoll, drama, memoir, anthology, nonfiction, essay


# ---------------
# Function calls
# ---------------
csv_list = get_csv_list(CSV_LOCATION)
author_ids, publications, places, countries, languages, genres, timeline, translations, english, french, spanish, dutch, portuguese, haitiancreole, italian, arabic, chinese, creole, czech, danish, estonian, finnish, frenchcreole, german, greek, greekmodern, hebrew, hungarian, japanese, korean, latvian, norwegian, persian, farsi, polish, romanian, russian, serbian, slovenian, spanishfrench, slucreole, swedish, turkish, vietnamese, welsh, fictionnovel, fictionstory, fictionstorycoll, poem, poetrycoll, drama, memoir, anthology, nonfiction, essay = process_author_files(CSV_LOCATION, csv_list, MAPBOX_USERNAME)

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

with codecs.open(ENGLISH_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(english, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(FRENCH_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(french, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(SPANISH_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(spanish, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(DUTCH_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(dutch, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(PORTUGUESE_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(portuguese, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(HAITIANCREOLE_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(haitiancreole, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(ITALIAN_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(italian, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(ARABIC_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(arabic, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(CHINESE_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(chinese, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(CREOLE_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(creole, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(CZECH_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(czech, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(DANISH_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(danish, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(CHINESE_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(chinese, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(ESTONIAN_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(estonian, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(FINNISH_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(finnish, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(FRENCHCREOLE_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(frenchcreole, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(GERMAN_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(german, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(GREEK_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(greek, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(GREEKMODERN_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(greekmodern, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(HEBREW_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(hebrew, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(HUNGARIAN_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(hungarian, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(JAPANESE_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(japanese, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(KOREAN_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(korean, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(LATVIAN_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(latvian, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(NORWEGIAN_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(norwegian, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(PERSIAN_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(persian, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(FARSI_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(farsi, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(POLISH_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(polish, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(ROMANIAN_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(romanian, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(RUSSIAN_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(russian, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(SERBIAN_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(serbian, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(SLOVENIAN_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(slovenian, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(SPANISHFRENCH_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(spanishfrench, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(SLUCREOLE_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(slucreole, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(TURKISH_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(turkish, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(VIETNAMESE_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(vietnamese, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(WELSH_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(welsh, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(FICTIONNOVEL_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(fictionnovel, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(FICTIONSTORY_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(fictionstory, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(FICTIONSTORYCOLL_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(fictionstorycoll, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(POEM_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(poem, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(POETRYCOLL_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(poetrycoll, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(DRAMA_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(drama, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(MEMOIR_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(memoir, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(ANTHOLOGY_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(anthology, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(NONFICTION_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(nonfiction, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()

with codecs.open(ESSAY_JSON, 'w', 'utf8') as f:
  f.write(json.dumps(essay, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
  f.close()