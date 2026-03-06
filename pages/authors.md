---
layout: pagedefault
title: "Authors"
permalink: /authors/
---

<!-- <div class="wordcloud">
	<img src="{{ site.baseurl }}/assets/img/bannerauthors.png"></div>
<div>-->
<head>
    <link rel="stylesheet" type="text/css" href="{{site.baseurl}}/assets/css/includes-style/browse-author-style.css">
    </head>
	
For each of the **{{site.data.biography | size}}+ authors** in our continuously growing dataset! They all have a profile that contains a brief biographical summary, with links to the author's <a href="https://www.wikipedia.org/" target="_blank">Wikipedia page</a> and various <a href="https://www.dloc.com/" target="_blank">DLOC resources</a>. The author bibliography is displayed as a scrollable vertical timeline in ascending order of publication.

Author profiles generally include new editions, translations and significant reprints of their original works.

###### Directions

Clicking on author's image will take you to their profiles.

You can search and filter our growing authors dataset. By typing into the search bar below. Or by creating a filter by first letter of their first name by clicking on the "name"  button and then selecting the search letter. You can also filter by country and then selecting your desired country.

The name and country sorting buttons can have one selected value at a time. But you can combine these filters to sort by country then by first name or vice versa.Selecting either button will turn it black to indicate that is active.

You can clear your filter by pressing the red "clear all filters" button below. Or by repressing your selection once again.



<div class="authors">
{% include updated-browse-authors.html %}
</div>
