---
---

const siteBaseUrl = "/vcl";







const link = document.getElementById("publicationLink");
const authorId = link.getAttribute("data-authorid");

$('.card-link').off('click').on('click', function(event) {
    event.preventDefault();
    showAuthorBio(authorId,authorName,authorCountry,publicationTitle,publicationDate,publicationPublisher,publicationGenre,publicationLanguage,publicationIsTranslation);
});






//Function that dynamically populates with the author's bio
function showAuthorBio(authorid,authorName,authorCountry,publicationTitle,publicationDate,publicationPublisher,publicationGenre,publicationLanguage,publicationIsTranslation) {

        
console.log(`look at me its me authorBio: ${authorid} here!`);
$('.content').html(`
<!--This create the first column div-->

<div class="col" style="position:relative;">

<!-- Creates a container so that the author's profile photo side can scroll independtly of the book details -->
<div class="authorbiodata" style="position: sticky; top: 68px;">
<div height="700px" width="500px">
<h3>${authorName}</h3>
<div class="authorimg">
<img src="${siteBaseUrl}/authorphotos/${authorid}.jpg" />
</div>   
<br>
<div class="authordetails">
<h6> <a href="${siteBaseUrl}/pages/Countries/${authorCountry}.md"><b>Country of Birth: </b>${authorCountry}</a> <br>
 <b>Lifespan:</b> {{author.Lifespan}} <br>
 <b> Biography: </b> <a href="{{author.Wikimedia}}">Learn More About the Author</a> <br>
 <b> DLOC Resources: </b><a href="${siteBaseUrl}/{{authorBio.authorid}}_dloc/"> Author Resources</a>
 </h6>
</div>
</div>
</div>
</div>

`);
console.log('ShowAuthorBio working here!');
showAuthorDetails(authorid,publicationTitle,publicationDate,publicationPublisher,publicationGenre,publicationLanguage,publicationIsTranslation);
  }












//Funciton that dynamically populates the author's book detail
function showAuthorDetails(authorid,publicationTitle,publicationDate,publicationPublisher,publicationGenre,publicationLanguage,publicationIsTranslation){
 
    console.log("showAuthorDetails saying hey here")


let htmlContent = `<div class="col" >`;


//i variable added to create an index count for the publications by each author


//console.log(`${key}${imgArray}`);        
htmlContent += `
<!-- For it to fully put in two columns i need to populate this into the div above -->
<div class="books">
<div style="margin-bottom:0; width:100%">
<div class="publication_date">    
<h3><b> Published in ${authorid}</b></h3>
</div>
<div class="bookphoto">  
<img src="${siteBaseUrl}/bookphotos/$${authorid}/${authorid}.jpg" style="display:block; margin-left: auto; margin-right:auto; width:50%;"/>
</div>
<div class="book_details">

<div class="publication_title">
{% for publication in site.data.publocation %}
<h5><b><i>{{publication.Title}}</i></b></h5>
{% endfor %}
</div>

<div class="publication_genre">
<p><b><a href="${authorid}">${authorid}</a>, <span><a href="${siteBaseUrl}/${authorid}/">${authorid}</a></span> </b></p>
</div>
<div class="publication_publisher">
<p><b>${authorid},<br> <span>Translation: ${authorid}</span></b></p>
</div>
</div><br>
<hr>
</div>
`;

htmlContent +=`</div>`;

//originallly #data-container not .content
$('.content').append(htmlContent);

}
