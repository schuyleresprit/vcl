---
layout: pagedefault
title: 'MapBox Workaround'
permalink: /mapboxworkaround/
---

# Details From Authors Page

For each of the **{{site.data.biography | size}}+ authors** in our continuously growing dataset! They all have a profile that contains a brief biographical summary, with links to the author's <a href="https://www.wikipedia.org/" target="_blank">Wikipedia page</a> and various <a href="https://www.dloc.com/" target="_blank">DLOC resources</a>. The author bibliography is displayed as a scrollable vertical timeline in ascending order of publication.

Author profiles generally include new editions, translations and significant reprints of their original works.


---

# Rationale / Explaination of MapBoxAPI Workaround 

Here is the workaround solution to the missing mapbbox api token. This solution depends on a spreadsheet (we can use google sheets to create and export the sheet into the VCL development folder), using Jekyll features such as the: '_data ' folder, '_include' folder , collection feature is Jekyll and the various Liquid templating tags and variables. It becomes easier to build a data-driven static website. 


This workaround allows us to continue working in google drive as a hub across Create Caribbean and the many projects. We add our author's biography, publication, and other resources like Wikipedia, DLOC, Youtube, Amazon etc dataset in their respective google sheets and we can choose to download the spreadsheet right from google sheets to the local host of VCL on the computers into the '_data' folder. 

With the use of Jekyll we do not have to convert the sheet into a specific JSON format for the code to work. We can download it as a csv file and Jekyll will process it and turn it a variable that can be accessed anywhere on the site !! The variable as the formatting of " {{site.data. DATA_FILE_NAME_WITHOUT_FILE_EXTENSION }} (without the spaces) " and filters such as 'sort', 'where' , 'group_by' , 'slice' etc

We can use the '_include' folder to create HTML Snippets that can be reused not only inside of VCL but other projects that uses Jekyll as well. For a plug and play kind of feeling. We can add a search bar, indexing letter tab, timelines, maps, audios, videos, exported twine games etc.

With Jekyll's ability to add 'Front Matter' which allows the file to be processed similar to other Jekyll features. So that means in a JavaScript (more than likely Python as well) file we can add the Liquid tags and variables in mixture with vanilla Javascript and other JavaScript libraries.

This workaround is also fixing the issue with not being able to reload, go back, or go forwoard once we dynamically loaded the author's bio and publication. 

This workaround also makes it easier to load multiple data from the '_data' folder so for example if I wanted to see everything we have related to an author based on the authorid in the 'biography.csv', 'publocation.csv' and 'additional-resources.csv' (Which are all located in the '_data' folder).



For this workaround I have created a new browse-author.html in the '_includes' folder temporaily named: 'browse-authors-edit.html' I have also created a file named 'loadAuthor.html' that will based on the authorid variable found in front matter of each author's markdown file load all the data found in the data files. Now the author's bio loads from the 'biography.csv' , the publication from the 'publocation.csv' and the author's DLOC/other related resources loads from the 'additional-resources.csv' 

The markdown files for each author is needed in order to run the code and those have to be created. I manually add 'A' authors for testing purposes. But I figure we can 
(i) create google app script that creates the markdown file for us. 
(ii) create a python script that utilizes the front matter processing features of Jekyll and create a file using similar tools to how we dynamically load the data anyway. {I think this would be better suited for Brandon}.

The same would be needed for the pagination , indexing etc once a user engages with these dynamically loaded functions we lose the ability to go backwards like we are accustomed to in HTML. Possible solutions to this problem is 
(i) creating markdown pages that allows us to dynamically use the functions but gives us a page that can interact with browser history
(ii) come up with a script solution that creates tracking points to save url history similar to the History Web API (The history falls sort because the information is dynamically loaded and has no tracking)

This workaround breaks the search bar and the indexing functionality, but I am working on getting those back as well as considering using LunrJS, like what is used in Wax, to create a more robust searching to match this projects Large interactive visualize database. 


{% include browse-authors-edit.html %}

