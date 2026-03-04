---
layout: pagedefault
title: Author Profile
permalink: /profile/
---

<head>
    <link rel="stylesheet" type="text/css" href="{{site.baseurl}}/assets/css/includes-style/browse-author-style.css">
    </head>

<div id="detail-root" class="detail-root container-fluid">
  <p>Loading…</p>
</div>

<!-- same data source -->
<script id="stakeholders-data" type="application/json">
  {{ site.data["biography"] | jsonify }}
</script>

<script>
(function(){
  const root = document.getElementById("detail-root");
  const safe = (x) => (x == null ? "" : String(x));
  const normalizeHeader = (h) => String(h||"").trim().toLowerCase()
    .replace(/&/g,"and").replace(/[@]/g,"at")
    .replace(/\s+/g,"_").replace(/[^\w]+/g,"_")
    .replace(/_+/g,"_").replace(/^_|_$/g,"");
  const slugify = (s) => String(s||"").trim().toLowerCase()
    .normalize("NFKD").replace(/[\u0300-\u036f]/g,"")
    .replace(/[^a-z0-9]+/g,"-").replace(/^-+|-+$/g,"");


//This creates a URL parameter that will be used to dynamically load the dataset and allows for a bettery history navigation than the previous
  function getParam(name){
    const url = new URL(window.location.href);
    return url.searchParams.get(name);
  }

//Gathering the data loaded by Jekyll in a script tag above this one
  function readData() {
    try { return JSON.parse(document.getElementById("stakeholders-data").textContent) || []; }
    catch(e){ console.error(e); return []; }
  }

  // Prepare data
  const RAW = readData();
  if (!RAW.length) { root.innerHTML = "<p>No data available.</p>"; return; }

  const HEADERS = Object.keys(RAW[0]).map(orig => {
    const label = String(orig||"").trim() || "(Unnamed column)";
    return { original: orig, key: normalizeHeader(label), label };
  });

  const DATA = RAW.map(row => {
    const out = {};
    for (const h of HEADERS) out[h.key] = safe(row[h.original]);
    out.slug = slugify(out.name || out.title || out.name_ || out["name_"]);
    return out;
  });



  //This section is what is used to load up the datasets related to the selected author.

  const id = getParam("id");
  //If id does not cointain a value it will return this messages
  if (!id) { root.innerHTML = "<p>Missing id.</p>"; return; }

    // locate by authorid
  const item = DATA.find(r => r.authorid === id);

  //If id does not match our dataset it will return
  if (!item) { root.innerHTML = "<p>Not found.</p>"; return; }

//Loading  publications,dLOC, and other dataset
//EDIT HERE TO CHANGE DATASETS
const masterPublications = {{site.data.publocation | sort:"Pubdate" | jsonify}};

const masterDLOC = {{site.data.additional-resources | jsonify}}

//Apply a filter to the additional datasets in order to lookup matching data fields to id,title etc.
const authorPublications = masterPublications.filter(r => r.authorid === item.authorid);
const authorDLOC = masterDLOC.filter(r => r.authorid === item.authorid);


  // fields (use your actual column set; these match the earlier script)
  const name       = item.name || "(No Name)";
  const country    = item.country;
  const typeCat    = item.type_category;
  const lifespan   = item.lifespan;
  const genreType  = item.genre_type;
  const wiki       = item.wikipedia_url_if_applicable;
  const imageUrl   = item.image_url;
  const dlocUrl    = item.dloc_items_url;
  const awards     = item.awards;
  const mediaAbout = item.media_about_them;
  const website    = item.website || item.site || ""; // just in case


console.log(item);
  // render detail view
  root.innerHTML = `
<!-- The div element that controls -->
<div class="row justify-content-center">

 <p class="backlink"><a href="{{site.baseurl}}/authors/">← Browse Authors</a></p>
    <!--This create the first column div-->
    
    <div class="col" style="position:relative;">
    
    <!-- Creates a container so that the author's profile photo side can scroll independtly of the book details -->

    
        <!-- 1st column containing the Author's Biography and Related Resources-->
        <div class="authorbiodata" style="position: sticky; top: 68px;">
        <div height="700px" width="500px">
            <h3>${name}</h3>
        <div class="authorimg">
            <img src="{{site.baseurl}}/authorphotos/${item.authorid}.jpg" />
        </div>   
    <br>
    
  
    <div class="authordetails">
    <h6> <b>Country of Birth: </b><a href="{{ site.baseurl }}/countries/${item.mapid}/">${country}</a> <br>
        <b>Lifespan:</b> ${lifespan} <br>
       
        <p>Read furthur details on the author's biography<a class="bioResourceLinks" href="${item.wikimedia}" target="_blank" > -sourced from Wikipedia</a></p>
        
        </h6>
    </div>
       
        </div>
    </div>
</div>
   
        
       
    
      <!-- Creates the 2nd column containing the Author's Publication(s) details-->
    <!-- For it to fully put in two columns i need to populate this into the div above -->
     <div class="col">
     
    <!-- Creates an collapse menu using Bootstrap -->
    
    <div class="accordion" id="creativeContribution">
    <div class="accordion-item">
    <h2 class="accordion-header">
    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#creativeContributionCollapse"  aria-controls="creativeContributionCollapse">
    Publication(s)
    </button>
    </h2>
    <div id="creativeContributionCollapse" class="accordion-collapse collapse" data-bs-parent="creativeContributionCollapse">
    <div id="creativeContributionBody" class="accordion-body">
   
    </div>
    </div>
    
    
    <div class="accordion" id="creativeDLOC">
    <div class="accordion-item">
    <h2 class="accordion-header">
    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#creativeDLOCCollapse"  aria-controls="creativeDLOCCollapse">
    Resources at Digital Library of The Caribbean
    </button>
    </h2>
    <div id="creativeDLOCCollapse" class="accordion-collapse collapse" data-bs-parent="creativeDLOCCollapse">
      <div id="creativeDLOCBody" class="accordion-body">

      </div>      
    </div>
    
    
    
    <div class="accordion" id="creativeMedia">
    <div class="accordion-item">
    <h2 class="accordion-header">
    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#creativeMediaCollapse"  aria-controls="creativeMediaCollapse">
    Media About ${name}
    </button>
    </h2>
    <div id="creativeMediaCollapse" class="accordion-collapse collapse" data-bs-parent="creativeMediaCollapse">
      <div class="accordion-body">
  
      </div>      
    </div>
    
    
    
    
    
    
    <!-- end tag for div that makes this two column-->
    </div>
    
    </div>

 `;

 //Breaking up the HTML in order to loop through all publications, dloc and any other data related to a specfic individual's profile.As well as since Jekyll is static built oriented and this functionailty is calling for a dynamic solution.
  const publicationCollapse = document.getElementById("creativeContributionBody");
  const dlocCollapse = document.getElementById("creativeDLOCBody");

authorPublications.forEach(
  details => {

 publicationCollapse.innerHTML += `
<div class="books">
   
    <h3 class="publication_date"><b>Published in ${details.Pubdate}</b></h3>

            <div id="publicationImageContainer">
            <img class="bookphoto" src="{{site.baseurl}}/bookphotos/${item.authorid}/${details.bookImgId}.jpg" />
            </div>

            <div class="book_details">
            <h4 class="publication_title"><b><i>${details.Title}</i></b></h4>
           
            <div class="publication_summary text_truncate">
                <p class="text-wrap text-truncate">${details.Summary}</p>
              </div>
              <hr />
            <div class="publication_details">
              <p class="publication_genre">
               
            <b><a href="{{site.baseurl}}/${encodeURIComponent(details.Genre)}">${details.Genre}</a></b>
                </p>
                <p class="publication_language"><b><a href="{{site.baseurl}}/${encodeURIComponent(details.Language)}">${details.Language}</a></b></p>
       
                 <p class="publication_publisher"><b>${details.Publisher}</b></p>
                 <p class="publication_translation"><b>${details.Translation}</b></p>
             </div>
        </div>

        <p class="publicationResourceLinks">
                <span><a id="Buy" href="${details.Buy_Link}" target="_blank">Buy</a></span>
                <span>|</span>
                <span><a id="Read" href="${details.Read_Link}" target="_blank">Read</a></span>
                <span>|</span>
                <span><a id="Listen" href="${details.Listen_Link}" target="_blank">Listen</a></span>
              </p>
<hr />
</div>

`});

authorDLOC.forEach(

details => {

switch(details.resource_type){

case "video" :
dlocCollapse.innerHTML += `
<h1>${details.resource_title}</h1>
 <video class="w-75 h-75" controls >
            <source src="${details.resource_url}">
        </video>
 <a href="${details.resource_source_url}" target="_blank"><p>View Resource Courtsey of dLOC</p></a>
<hr />
`;
break;
case "audio" :
  dlocCollapse.innerHTML += `
<h1>${details.resource_title}</h1>
  <audio controls>
            <source src="${details.resource_url}">
        </audio>
 <a href="${details.resource_source_url}" target="_blank"><p>View Resource Courtsey of dLOC</p></a>
<hr />
`;
break;
case "image":
   dlocCollapse.innerHTML += `
  <h1>${details.resource_title}</h1>
  <div id="publicationImageContainer">
  <img class="bookphoto" src="${details.resource_url}" />
</div>
 <a href="${details.resource_source_url}" target="_blank"><p>View Resource Courtsey of dLOC</p></a>
<hr />
`;
break;
case "pdf":
     dlocCollapse.innerHTML += `
  <h1>${details.resource_title}</h1>
<a href="${details.resource_source_url}" target="_blank"><p>View PDF Resource Courtsey of dLOC</p></a>
<hr />
`;
break;
case "website":
       dlocCollapse.innerHTML += `
  <h1>${details.resource_title}</h1>
  <iframe width="100%" height="50%" src="${details.resource_url}"></iframe>
<a href="${details.resource_source_url}" target="_blank"><p>View Resource Courtsey of dLOC</p></a>
<hr />
`;
break;
case "embed":
         dlocCollapse.innerHTML += `
  <h1>${details.resource_title}</h1>
  ${details.resource_url}
<a href="${details.resource_source_url}" target="_blank"><p>View Resource Courtsey of dLOC</p></a>
<hr />
`;
break;
default: 
dlocCollapse.innerHTML += `
<p>No dLOC Resources Located</p>

`;
}});

})();
</script>

<style>
.detail-root { margin-top: 1rem; }
.detail-wrap { 
  display:grid; grid-template-columns: 1fr 2fr; gap: 1.25rem; 
  align-items:start;
}
@media (max-width: 900px) {
  .detail-wrap { grid-template-columns: 1fr; }
}
.detail-media { background:#f3f3f3; border:1px solid #ddd; border-radius:10px; overflow:hidden; }
.detail-media img { width:100%; height:auto; display:block; }
.detail-placeholder { width:100%; aspect-ratio: 4 / 3; background:#e5e5e5; }

.detail-info { 
  border:1px solid #ddd; border-radius:10px; padding:1rem; background:#fff;
}
.detail-title { margin:0 0 .25rem 0; }
.pill { display:inline-block; padding:.2rem .5rem; border-radius:999px; font-size:.9rem; background:#f6f6f6; border:1px solid #eee; }

.detail-grid { display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:.5rem .75rem; margin:.75rem 0; }
.detail-links { display:flex; flex-wrap:wrap; gap:.5rem .75rem; margin: .5rem 0 1rem; }
.detail-links a { text-decoration:none; border:1px solid #ddd; border-radius:8px; padding:.35rem .6rem; background:#fafafa; }
.detail-links a:hover { border-color:#c5c5c5; }

.backlink a { text-decoration:none; }
</style>
