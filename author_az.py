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
CATEGORY_JSON = os.path.join(DATA_DIR, 'category.json')
KEYWORDS_JSON = os.path.join(DATA_DIR, 'keywords.json')

# ----------
# Functions
# ----------

# Returns a list of all the csv files in a directory
def get_csv_list(csv_location):
    return [file for file in os.listdir(csv_location) if file.lower().endswith('.csv')]

def process_heritage_words(csv_path, csv_list):
    # Initialize dictionaries
    letters_dict = {chr(i): {} for i in range(ord('a'), ord('z') + 1)}
    categories = {}
    keywords = {}

    # Unique ID counter
    unique_id_counter = 1

    # Process each CSV file
    for csv_name in csv_list:
        with open(os.path.join(csv_path, csv_name), 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)

            # Iterate over each row in the CSV file
            for row in reader:
                # Extract heritage word information
                title = row['Title']
                description = row['Description']
                category = row['Category Description']
                keyword = row['Keywords']

                # Determine the starting letter of the title
                letter = title.lower()[0] if title else None

                # Create a unique ID for the current row
                unique_id = f"id_{unique_id_counter}"
                unique_id_counter += 1

                # Organize heritage words by starting letter
                if letter and letter in letters_dict:
                    heritage_word_info = {
                        'ID': unique_id,
                        'Title': title,
                        'Description': description,
                        'Category': category,
                        'Keywords': keyword
                    }
                    letters_dict[letter][unique_id] = heritage_word_info

                # Organize heritage words by category
                if category:
                    if category not in categories:
                        categories[category] = []
                    categories[category].append(heritage_word_info)

                # Organize heritage words by keywords
                if keyword:
                    if keyword not in keywords:
                        keywords[keyword] = []
                    keywords[keyword].append(heritage_word_info)

    # Write letter data to separate JSON files
    for letter, data in letters_dict.items():
        with codecs.open(JSON_FILES[letter], 'w', 'utf-8') as json_file:
            json.dump(data, json_file, indent=4, separators=(',', ': '), ensure_ascii=False)

    # Write data to separate JSON files for category and keywords
    with codecs.open(CATEGORY_JSON, 'w', 'utf-8') as json_file:
        json.dump(categories, json_file, indent=4, separators=(',', ': '), ensure_ascii=False)

    with codecs.open(KEYWORDS_JSON, 'w', 'utf-8') as json_file:
        json.dump(keywords, json_file, indent=4, separators=(',', ': '), ensure_ascii=False)

    return letters_dict, categories, keywords

# Function calls
csv_list = get_csv_list(CSV_LOCATION)
letters_dict, categories, keywords = process_heritage_words(CSV_LOCATION, csv_list)
