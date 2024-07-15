//search bar functionality

document.querySelector('.searchForm').addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent form submission from reloading the page

    const input = document.querySelector('.searchInput').value.trim().toLowerCase();
    const contentDiv = document.querySelector('.content');

    if (input) {
        contentDiv.innerHTML = `Search results for "${input}":`;

        // Fetch data from JSON file
        fetch(`data/${input.charAt(0)}.json`)
            .then(response => response.json())
            .then(data => {
                // Filter entries 
                const filteredEntries = Object.values(data).filter(entry => entry.Title.toLowerCase().includes(input));

                // Display filtered entries
                filteredEntries.forEach(entry => {
                    const gridItem = document.createElement('div');
                    gridItem.className = 'grid-item';
                    gridItem.innerHTML = `
                        <h3>${entry.Title}</h3>
                        <p>${entry.Description}</p>
                    `;
                    contentDiv.appendChild(gridItem);
                });
            })
            .catch(error => {
                console.error('Error fetching or parsing data:', error);
                contentDiv.innerHTML = 'Error loading search results.';
            });
    } else {
        contentDiv.innerHTML = "Please enter a search query.";
    }
});



// index button on nav panel

document.querySelectorAll('.button-container button').forEach(button => {
    button.addEventListener('click', () => {
        const filePath = button.getAttribute('data');
        const contentDiv = document.querySelector('.content');

        fetch(filePath)
            .then(response => response.json())
            .then(data => {
                
                // Clear content
                contentDiv.innerHTML = '';

                // Create each word element
                Object.values(data).forEach(entry => {
                    const gridItem = document.createElement('div');
                    gridItem.className = 'grid-item';
                    gridItem.innerHTML = `
                        <h3>${entry.Title}</h3>
                        <p>${entry.Description}</p>
                    `;
                    contentDiv.appendChild(gridItem);
                });
            })
            .catch(error => {
                console.error('Error fetching or parsing data:', error);
                contentDiv.innerHTML = 'Error loading content.';
            });
    });
});



//previous script

