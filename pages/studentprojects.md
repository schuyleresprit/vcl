---
layout: pagedefault
title: "Student Projects"
permalink: /studentprojects/
---
<head>
<link rel="stylesheet" type="text/css" href="{{site.baseurl}}/assets/css/includes-style/browse-author-style.css">
</head>

The individual student projects completed under the theme Visualizing Caribbean Literature are as vast and diverse as the idea of Caribbean literature itself. The students’ work reflects their attention to the complexity and variety of experiences and stories of Caribbean being - in the past, present and future. Student projects have been organized into three broad categories.

###### Directions
Clicking on the card will lead you to the student projects.

Clicking on the students name will lead you to their websites.

<div class="row justify-content-center content">
    {% for details in site.data.student-projects %}
    <div class="card col-4">
      <div class="card-body">  
       <!-- <h6 class="card-subtitle">${data.subtitle}</h6> -->
       <img id="authorImgCard" src="{{ details.student_photo }}" />
       <h6 class="card-title">{{ details.student_name }}</h6>
        <h6 class="card-subtitle">{{ details.project_title }}</h6>
        <br />
        <h6 class="card-subtitle">{{ details.project_category }}</h6>
        <a href="{{ details.student_project_url}}" class="card-link" target="_blank"> View Project</a>
    </div> 
    </div>
    {% endfor %}