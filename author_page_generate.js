const fs = require('fs');
const path = require('path');

function generatePages() {
    let data;
    
    // Load data from JSON file
    try {
        const dataPath = path.join('data', 'publications.json');
        const jsonData = fs.readFileSync(dataPath, 'utf-8');
        data = JSON.parse(jsonData);
    } catch (err) {
        if (err.code === 'ENOENT') {
            console.error("The file data/publications.json was not found.");
        } else if (err instanceof SyntaxError) {
            console.error("Error decoding JSON from the file.");
        } else {
            console.error("An unknown error occurred:", err);
        }
        return;
    }

    // Create the output directory if it doesn't exist
    const outputDir = path.join(__dirname, 'output');
    if (!fs.existsSync(outputDir)) {
        fs.mkdirSync(outputDir);
    }

    // Iterate through each author ID in the JSON data
    for (const authorid in data) {
        if (data.hasOwnProperty(authorid)) {
            const authorPublications = data[authorid];
            
            // Generate HTML content
            let htmlContent = `
            ---
            layout: defaultau
            title: ${authorid} Author Name 
            permalink: /${authorid}
            ---
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Author Details - ${authorid}</title>
            </head>
            <body>
                <h1>Author Details - ${authorid}</h1>
            `;
            
            for (const publication of authorPublications) {
                htmlContent += `
                <ul>
                    <li><strong>Title:</strong> ${publication['Title']}</li>
                    <li><strong>Genre:</strong> ${publication['Genre']}</li>
                    <li><strong>Language:</strong> ${publication['Language']}</li>
                    <li><strong>Publisher:</strong> ${publication['Publisher']}</li>
                    <li><strong>Publication City:</strong> ${publication['Pub_id']}</li>
                    <li><strong>Publication Date:</strong> ${publication['Pubdate']}</li>
                    <li><strong>Translation:</strong> ${publication['Translation']}</li>
                </ul>
                <hr>
                `;
            }
            
            htmlContent += `
            </body>
            </html>
            `;
            
            // Write HTML content to a file
            const outputFilePath = path.join(outputDir, `${authorid}.md`);
            fs.writeFileSync(outputFilePath, htmlContent);

            console.log(`Output page generated for Author ID: ${authorid}`);
        }
    }
}

// Generate pages for all authors
generatePages();
