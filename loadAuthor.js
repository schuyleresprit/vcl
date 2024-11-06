
      $('.card-link').off('click').on('click', function(event) {
            event.preventDefault();
            const authorId = $(this).data('authorid');
            showAuthorBio(authorId);
        });

const datasets = [
    {
    type: "authors",
    url: "/vcl/data/authors.json"
 }
            
];

const dataLinks = [];


//Calling a jQuery to load the data as the page is loaded

          $(document).ready(function(){
           datasets.forEach(dataset => {
            siftData(dataset.url, dataset.type, function(data){
                dataLinks.push({
                    type: dataset.type,
                    data: data
                });
            });
               // setTimeout(() => showCategory(), 1000);
            }); 
        });



        function siftData(url, dataType, callback) {
            $.getJSON(url, function(data) {
                const temp = [];
                if (dataType === "authors") {
                    for (const key in data){
                    if(data.hasOwnProperty(key)){
                        temp.push({
                            flavorText: data[key].Author,
                            subtitle: data[key].author_country,
                            link: data[key].author_id
                        });
    
                    } 
                }
            }
                
                   callback(temp);
            });
        };



//Function that dynamically populates with the author's bio
function showAuthorBio(authorId) {
       const url = "{{ site.baseurl }}/data/bios.json";
       $.getJSON(url,function(data) {
        const authorBio = data[authorId];
if(authorBio){
console.log(`look at me its me authorBio: ${authorBio.authorid} here!`);
let htmlContent =`
<!--This create the first column div-->

<div class="col" style="position:relative;">

<!-- Creates a container so that the author's profile photo side can scroll independtly of the book details -->
<div class="authorbiodata" style="position: sticky; top: 68px;">
<div height="700px" width="500px">
<h3>${authorBio.Author} </h3>
<div class="authorimg">
<img src="{{site.baseurl}}/authorphotos/${authorBio.authorid}.jpg" />
</div>   
<br>
<div class="authordetails">
<h6> <b>Country of Birth: </b> ${authorBio.Country} <br>
    <b>Lifespan:</b> ${authorBio.Lifespan} <br>
    <b> Biography: </b> <a href="${authorBio.Wikimedia}">Learn More About the Author</a> <br>
    <b> DLOC Resources: </b><a href="{{site.baseurl}}/${authorBio.authorid}_dloc/"> Author Resources</a>
    </h6>
</div>
</div>
</div>
</div>

`;
console.log('ShowAuthorBio working here!');
$('.content').html(htmlContent)
showAuthorDetails(authorId);
     }
         else {
    console.error("Author not found in the data.");
      }
})
          .fail(function(){
            console.error("Failed to load JSON data.");
                     });
                                        
}




//Funciton that dynamically populates the author's book detail
function showAuthorDetails(authorId){
    const url = "{{ site.baseurl }}/data/publications.json";
 
     $.getJSON(url, function(data){
   //const authorPublications = data[authorId];
   for (const key in data){
   if(data.hasOwnProperty(key)){
    //console.log(`Key: ${key}, Value: ${JSON.stringify(data[key])}`);
   
   if(key === authorId){
    const authorPublications = data[key];
    console.log(`${key} is ${authorId}`);

     
    
if(Array.isArray(authorPublications))
   //if (authorPublications) 
   {
    console.log(`look at me its me authorPublications: ${authorPublications.Title} here!`);
//This will sort the books by Publication date

authorPublications.sort((a,b)=> new Date(a.Pubdate) - new Date(b.Pubdate));
let htmlContent = `<div class="col" >`;

authorPublications.forEach((publication, i) => {

//i variable added to create an index count for the publications by each author

let imgArray = i + 1; 
//console.log(`${key}${imgArray}`);        
htmlContent += `
<!-- For it to fully put in two columns i need to populate this into the div above -->
<div class="books">
<div style="margin-bottom:0; width:100%">
<div class="publication_date">    
<h3><b> Published in ${publication.Pubdate}</b></h3>
</div>
<div class="bookphoto">  
<img src="{{site.baseurl}}/bookphotos/${publication.Author}/${key}${imgArray}.jpg" style="display:block; margin-left: auto; margin-right:auto; width:50%;"/>
</div>
<div class="book_details">
<div class="publication_title">
<h5><b><i>${publication.Title}</i></b></h5>
</div>
<div class="publication_genre">
<p><b><a href="{{site.baseurl}}/${publication.Genre}/">${publication.Genre}</a>, <span><a href="{{site.baseurl}}/${publication.Language}/">${publication.Language}</a></span> </b></p>
</div>
<div class="publication_publisher">
<p><b>${publication.Publisher},<br> <span>Translation: ${publication.Translation}</span></b></p>
</div>
<p>This is: ${key}${imgArray}</p>
</div><br>
<hr>
</div>
`;
});

htmlContent +=`</div>`;

//originallly #data-container not .content
 $('.content').append(htmlContent);

} 
        
else {
            console.error("Publications not found for author.");
        }
    }
} 
}

}) 
       .fail(function(){
        console.error("Failed to load JSON data.");
       });
    }