let currentPage = 1;
const itemsPerPage = 30;
let allEntries = [];

// Function to fetch data for a specific letter from data folder
function fetchData(letter) {
    return fetch(`/vcl/data/${letter}.json`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => Object.values(data))
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            return [];
        });
}

// Function to load all data when the page loads
function loadAllData() {
    const letters = 'abcdefghijklmnopqrstuvwxyz'.split('');
    const promises = letters.map(letter => fetchData(letter));

    Promise.all(promises).then(results => {
        allEntries = results.flat();
        displayEntries();
    });
}

// Function to display entries based on the current page
function displayEntries() {
    const contentDiv = document.querySelector('.content');
    contentDiv.innerHTML = '';

    const startIndex = (currentPage - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
    const paginatedEntries = allEntries.slice(startIndex, endIndex);

    paginatedEntries.forEach(entry => {

        /*const gridItem = document.createElement('div');
        gridItem.className = 'grid-item';
        gridItem.innerHTML = `
            <h3>${entry.Title}</h3>
            <p>${entry.Description}</p>
            




        ``;
        contentDiv.appendChild(gridItem);
        */

//Setting the current page of the displayEntries() to the first page so that it loads the entries properly
        currentPage = 1;

//Instead of defining an HTML content for the displayEntries() call on the appendData()
//Creating the parameters that the appendCard() function is expecting to execute

const data = {

    flavorText: entry["Author Name"],
    subtitle: entry.Country,
    link: entry.Author_id
}
appendCard(data);

    });

    if (paginatedEntries.length === 0) {
        contentDiv.innerHTML = '<div><p>No matches found.</div></p>';
    }

    updatePagination();
}

// Function to update pagination controls
function updatePagination() {
    const pagination = document.getElementById('pagination');
    pagination.innerHTML = '';

    const totalPages = Math.ceil(allEntries.length / itemsPerPage);

    for (let i = 1; i <= totalPages; i++) {
        const pageItem = document.createElement('button');
        pageItem.textContent = i;
        pageItem.className = i === currentPage ? 'active' : '';
        pageItem.addEventListener('click', () => {
            currentPage = i;
            displayEntries();
        });
        pagination.appendChild(pageItem);
    }
}

// Function to filter entries based on search term and display
function searchEntries(searchTerm) {
    const filteredEntries = allEntries.filter(entry => entry["Author Name"].toLowerCase().includes(searchTerm));
    
    filteredEntries.forEach( entry => { 

    currentPage = 1; // Reset to first page on new search
    allEntries = filteredEntries;
    displayEntries();
});
}

// Load initial data when the page loads
window.onload = () => {
    loadAllData();
};

// Add event listener for the search form
document.querySelector('#searchInput').addEventListener('input', (event) => {
    event.preventDefault(); // Prevent form submission from reloading the page

    //const input = document.querySelector('.searchInput').value.trim().toLowerCase();
    const input = event.target.value.toLowerCase();

    if (input) {
        searchEntries(input);
    } else {
        alert('Please enter a term');
    }
});

// Add event listener for the index buttons on the nav panel
document.querySelectorAll('.button-container button').forEach(button => {
    button.addEventListener('click', () => {
        const letter = button.getAttribute('data-letter');
        const contentDiv = document.querySelector('.content');
        const filePath = `/vcl/data/${letter}.json`

        fetch(filePath)
            .then(response => response.json())
            .then(data => {
                // Clear content
                contentDiv.innerHTML = '';

                Object.values(data).forEach(entry => {
                
                allEntries = Object.values(data);
                displayEntries();

                // Create each word element
                /*
                Object.values(data).forEach(entry => {
                    const gridItem = document.createElement('div');
                    gridItem.className = 'grid-item';
                    gridItem.innerHTML = `
                        <h3>${entry.Title}</h3>
                        <p>${entry.Description}</p>
                    `;
                    contentDiv.appendChild(gridItem);
                    */
                });
            })
            .catch(error => {
                console.error('Error fetching or parsing data:', error);
                contentDiv.innerHTML = 'Error loading content.';
            });
    });
});
