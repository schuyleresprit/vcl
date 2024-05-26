document.addEventListener("DOMContentLoaded", function() {
    const cards = document.querySelectorAll('.card'); // Assuming each card has an 'author-id' attribute

    cards.forEach(card => {
        card.addEventListener('click', function() {
            const authorId = this.getAttribute('author-id');
            fetchAuthorData(authorId);
        });
    });

    function fetchAuthorData(authorId) {
        const fileName = `${authorId}.json`; // Assuming file names correspond to author IDs
        fetch(`separated_json/${fileName}`)
        .then(response => response.json())
        .then(data => {
            createPage(authorId, data); // Passing author ID as page title
        })
        .catch(error => console.error(`Error fetching data from ${fileName}:`, error));
    }

    function createPage(title, books) {
        const content = document.getElementById('content');
        content.innerHTML = ''; // Clear existing content

        const page = document.createElement('div');
        page.classList.add('page');
        page.innerHTML = `<h1>${title}</h1>`;

        books.forEach(book => {
            const bookDetails = document.createElement('div');
            bookDetails.classList.add('book-details');

            bookDetails.innerHTML = `
                <h2>${book.title}</h2>
                <p><strong>Author:</strong> ${book.author}</p>
                <p><strong>Date:</strong> ${book.date}</p>
                <p><strong>Language:</strong> ${book.language}</p>
                <p><strong>Genre:</strong> ${book.genre}</p>
                <p><strong>Translation:</strong> ${book.translation}</p>
                <p><strong>Publisher:</strong> ${book.publisher}</p>
                <p><strong>Number of Pages:</strong> ${book.pages}</p>
                <img src="${book.image}" alt="Book Cover">
            `;

            page.appendChild(bookDetails);
        });

        content.appendChild(page);
    }
});
