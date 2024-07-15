import os
import csv
import codecs
import json

# ---------
# Settings
# ---------

BASE_DIR = os.getcwd()
CSV_LOCATION = os.path.join(BASE_DIR, 'raw_data')
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Ensure the data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

#JSON file paths
JSON_FILES = {chr(i): os.path.join(DATA_DIR, f'{chr(i)}.json') for i in range(ord('a'), ord('z') + 1)}
AUTHORCOUNTRY_JSON = os.path.join(DATA_DIR, 'country.json')


# ----------
# Functions
# ----------

# Returns a list of all the csv files in a directory
def get_csv_list(csv_location):
    return [file for file in os.listdir(csv_location) if file.lower().endswith('.csv')]

def process_author_info(csv_path, csv_list):
    # Initialize dictionaries
    letters_dict = {chr(i): {} for i in range(ord('a'), ord('z') + 1)}
    categories = {}
    
    # Unique ID counter
    unique_id_counter = 1

    # Process each CSV file
    for csv_name in csv_list:
        with open(os.path.join(csv_path, csv_name), 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)

            # Iterate over each row in the CSV file
            for row in reader:
                # Extract author information
                author_name = row['Author']
                author_id= row['author_id']
                country = row['author_country']
                

                # Determine the starting letter of the author's name
                letter = author_name.lower()[0] if author_name else None

                # Create a unique ID for the current row
                unique_id = f"id_{unique_id_counter}"
                unique_id_counter += 1

                # Organize authors by starting letter
                if letter and letter in letters_dict:
                    author_info = {
                        'ID': unique_id,
                        'Author Name': author_name,
                        'Author_id': author_id,
                        'Country': country,
                    }
                    letters_dict[letter][unique_id] = author_info

                # Organize authors by country
                if country:
                    if country not in categories:
                        categories[country] = []
                    categories[country].append(author_info)


    # Write letter data to separate JSON files
    for letter, data in letters_dict.items():
        with codecs.open(JSON_FILES[letter], 'w', 'utf-8') as json_file:
            json.dump(data, json_file, indent=4, separators=(',', ': '), ensure_ascii=False)

    # Write data to separate JSON files for category: country
    with codecs.open(AUTHORCOUNTRY_JSON, 'w', 'utf-8') as json_file:
        json.dump(categories, json_file, indent=4, separators=(',', ': '), ensure_ascii=False)

    return letters_dict, categories

# Function calls
csv_list = get_csv_list(CSV_LOCATION)
letters_dict, categories= process_author_info(CSV_LOCATION, csv_list)
