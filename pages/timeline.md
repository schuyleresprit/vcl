---
layout: pagedefault
title: "Timeline"
permalink: /timeline/
---

<hr />


The Timeline visualizations showcases the span of time for Caribbean Literature


##### Directions
Use the horizontal scrollbar to view the timeline. 


<br />
<hr />

{% for details in site.data.additional-resources %}

{% assign resource_url = details.resource_url | split: ";" %}

{% for dloc in resource_url %}
<iframe width="25%" src="{{dloc.resource_url}}"></iframe>
{%endfor%}
{%endfor%}