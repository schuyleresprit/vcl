import csv
import sys
from util import QueueFrontier, Node

# Define global dictionaries to store data
authors = {}
titles = {}
genres = {}
languages = {}
author_countries = {}
publishers = {}
names = {}

def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load authors
    with open(f"{directory}/data/publications.json", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            author_id = row["author_id"]
            author_name = row["Author"]
            title_id = row["title_id"]
            title_name = row["title"]
            genre = row["genre"]
            language = row["language"]
            country = row["country"]
            publisher = row["publisher"]
            
            authors.setdefault(author_id, {"name": author_name, "titles": set()})
            authors[author_id]["titles"].add(title_id)
            
            titles.setdefault(title_id, {"name": title_name, "genre": genre, "language": language, "publisher": publisher})

            name_key = author_name.lower()
            names.setdefault(name_key, set()).add(author_id)

            genres.setdefault(genre, set()).add(author_id)
            languages.setdefault(language, set()).add(author_id)
            author_countries.setdefault(country, set()).add(author_id)
            publishers.setdefault(publisher, set()).add(author_id)

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python sixdeg2.py [data/publications.json]")
    directory = sys.argv[1]

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    # User interaction
    while True:
        print("\nSearch options:")
        print("1. Search by genre")
        print("2. Search by language")
        print("3. Search by author country")
        print("4. Search by publisher")
        print("5. Six Degrees of Separation")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            search_by_genre()
        elif choice == "2":
            search_by_language()
        elif choice == "3":
            search_by_country()
        elif choice == "4":
            search_by_publisher()
        elif choice == "5":
            six_degrees_of_separation()
        elif choice == "6":
            sys.exit("Exiting...")
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

def search_by_genre():
    genre = input("Enter genre: ")
    if genre not in genres:
        print("Genre not found.")
        return
    print("Authors in this genre:")
    for author_id in genres[genre]:
        print(authors[author_id]["name"])

def search_by_language():
    language = input("Enter language: ")
    if language not in languages:
        print("Language not found.")
        return
    print("Authors who write in this language:")
    for author_id in languages[language]:
        print(authors[author_id]["name"])

def search_by_country():
    country = input("Enter country: ")
    if country not in author_countries:
        print("Country not found.")
        return
    print("Authors from this country:")
    for author_id in author_countries[country]:
        print(authors[author_id]["name"])

def search_by_publisher():
    publisher = input("Enter publisher: ")
    if publisher not in publishers:
        print("Publisher not found.")
        return
    print("Authors published by this publisher:")
    for author_id in publishers[publisher]:
        print(authors[author_id]["name"])

def six_degrees_of_separation():
    # Implement the six degrees of separation game
    pass

if __name__ == "__main__":
    main()
