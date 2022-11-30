import csv
import sys
import json
from util import StackFrontier, QueueFrontier
from util import  Node


countries = {}
authors = {}
languages = {}
genres = {}
names = {}
titles = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load authors
    with open(f"data/publications.json", encoding="utf-8") as f:
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

    # Load languages
    with open(f"{directory}/data/languages.json", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                authors[row["author_id"]]["title"].add(row["title_id"])
                titles[row["title_id"]]["language"].add(row["author_id"])
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

    source =  author_id_for_name(input("Name: "))
    if source is None:
        sys.exit("author not found.")
    target = author_id_for_name(input("Name: "))
    if target is None:
        sys.exit("author not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            author1 = authors[path[i][1]]["name"]
            author2 = authors[path[i + 1][1]]["name"]
            title = titles[path[i + 1][0]]["title"]
            print(f"{i + 1}: {author1} and {author2} starred in {title}")


def shortest_path(source, target):
    """
    Returns the shortest list of (title_id, author_id) pairs
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
        children = neighbors_for_author(node.state)
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


def author_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    author_ids = list(names.get(name.lower(), set()))
    if len(author_ids) == 0:
        return None
    elif len(author_ids) > 1:
        print(f"Which '{name}'?")
        for author_id in author_ids:
            author = authors[author_id]
            name = author["name"]
            birth = author["birth"]
            print(f"ID: {author_id}, Name: {name}, Birth: {birth}")
        try:
            author_id = input("Intended author ID: ")
            if author_id in author_ids:
                return author_id
        except ValueError:
            pass
        return None
    else:
        return author_ids[0]


def neighbors_for_author(author_id):
    """
    Returns (title_id, author_id) pairs for authors
    who starred with a given author.
    """
    title_ids = authors[author_id]["titles"]
    neighbors = set()
    for title_id in title_ids:
        for author_id in titles[title_id]["stars"]:
            neighbors.add((title_id, author_id))
    return neighbors


if __name__ == "__main__":
    main()
