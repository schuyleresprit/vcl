import csv
import sys
import json
import Node
from python_utils import QueueFrontier
from python_utils import StackFrontier
 


# Maps names to a set of corresponding author_country
countries = {}

# Maps author_ids to a dictionary of: name, title, pubdate,  publisher
authors = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
languages = {}

genres = {}
names = {}
titles = {}
#


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load authors
    with open(f"{directory}/data/authors.json", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            authors[row["id"]] = {
                "name": row["Author"],
                "author_id": row["author_id"],
                "titles": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load titles
    with open(f"{directory}data/publications.json", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            titles[row["id"]] = {
                "title": row["title"],
                "year": row["Pubdate"],
                "language": set()
            }

    # Load stars
    with open(f"{directory}/data/languages.json", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                authors[row["person_id"]]["title"].add(row["movie_id"])
                titles[row["movie_id"]]["language"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = authors[path[i][1]]["name"]
            person2 = authors[path[i + 1][1]]["name"]
            movie = titles[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    solution_found = False
    no_solution = False
    solution = list()

    initial = Node(state=source, parent=None, action=None)
    frontier = QueueFrontier()
    frontier.add(initial)
    explored = set()
    i = 0
    while solution_found == False:

        if frontier.empty() == True:
            no_solution = True
            solution_found = True

        node = frontier.remove()
        # print("\n\nNode in= ",node, ' i=', i)

        if node.state == target:
            # Return the solution
            solution_found = True
            while node.parent is not None:
                pid, mid = node.state, node.action
                solution.append((mid, pid))
                node = node.parent
            solution.reverse()

        explored.add(node)
        children = neighbors_for_person(node.state)
        for child in children:
            child_node = Node(state=child[1], action=child[0],parent=node)
            frontier.add(child_node)
            if child_node.state == target:
                # Return the solution
                solution_found = True
                while child_node.parent is not None:
                    pid, mid = child_node.state, child_node.action
                    solution.append((mid, pid))
                    child_node = child_node.parent
                solution.reverse()

    if solution_found == True:
        if no_solution == True:
            return None
        return solution


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = authors[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for authors
    who starred with a given person.
    """
    movie_ids = authors[person_id]["titles"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in titles[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
