import json
import os

def generate_pages():
    try:
        # Load data from JSON file
        with open('data/publications.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("The file data/publications.json was not found.")
        return

    except json.JSONDecodeError:
        print("Error decoding JSON from the file.")
        return

    # Create the output directory if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')

    # Iterate through each author ID in the JSON data
    for authorid, author_publications in data.items():
        # Generate HTML content
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Author Details - {authorid}</title>
        </head>
        <body>
            <h1>Author Details - {authorid}</h1>
        """
        
        for publication in author_publications:
            html_content += f"""
            <ul>
                <li><strong>Title:</strong> {publication['Title']}</li>
                <li><strong>Author:</strong> {publication['Author']}</li>
                <li><strong>Descriptor:</strong> {publication.get('Descriptor', 'N/A')}</li>
                <li><strong>Genre:</strong> {publication['Genre']}</li>
                <li><strong>Language:</strong> {publication['Language']}</li>
                <li><strong>Pub ID:</strong> {publication['Pub_id']}</li>
                <li><strong>Pubdate:</strong> {publication['Pubdate']}</li>
                <li><strong>Publisher:</strong> {publication['Publisher']}</li>
                <li><strong>Translation:</strong> {publication['Translation']}</li>
            </ul>
            <hr>
            """
        
        html_content += """
        </body>
        </html>
        """
        
        # Write HTML content to a file
        output_file_path = os.path.join('output', f'{authorid}.html')
        with open(output_file_path, 'w') as output_file:
            output_file.write(html_content)
        
        print(f"Output page generated for Author ID: {authorid}")

# Generate pages for all authors
generate_pages()
