---
layout: default
title: English
permalink: /English/
---

<style>
.img-fluid {
    max-width: 100%;
    min-height: 500px;
    max-height: 500px;
}
</style>


<div class="individual_language">
<div class="background">
<div class="overlay">
<div class="row">
<div class="col-sm-1">
</div>
<div class="col-sm-10">
<div class="page_title"><h3>English</h3></div>

Represented here are the authors who have written works in English. Some of these may be texts translated into English from other languages.

<html>
<body>
	<div class="container">
		<div class="input-group mb-3">
			<input id="search-box" type="text" class="form-control" placeholder="Search for a title or author">
		</div>
		<div>
        <h5>Return to <a href="{% link pages/languages.md %}">Languages</a></h5>
        </div>
		<div id="data-container" class="row">
		</div>
	</div>
	<script>
		$( document ).ready(function() {
			//Set triggers
			$('#search-box').on('input', function (event) {
				showCategory(event.target.value);
			})
			//Populate page
			setTimeout(showCategory, 1000);
		});
		function showCategory (filter = "") {
			$('#data-container').html('');
			filter = filter.trim();
			$.getJSON("{{ site.baseurl }}/data/english.json", function (data) {
				let cards = [];
				for (const [key, value] of Object.entries(data)) {
					if (filter == "" && value.length > 0) {
						for (i = 0; i < value.length; i++) {
							//Todo:
							cards.push({
								"flavorText" : value[i]["Title"],
								"subtitle" : value[i]["Author"],
								"translation" : (value[i]["Translation"] == "y" ? "Translation" : ""),
								"link" : key,
							});
						}
					} else {
						for (i = 0; i < value.length; i++) {
							//TODO: Search Translation
							if (value[i]["Title"].toLowerCase().includes(filter.toLowerCase()) || value[i]["Author"].toLowerCase().includes(filter.toLowerCase())) {
								//Todo:
								cards.push({
									"flavorText" : value[i]["Title"],
									"subtitle" : value[i]["Author"],
									"translation" : (value[i]["Translation"] == "y" ? "Translation" : ""),
									"link" : key,
								});
							}
						}
					}
				}
				//Show Cards
				for (i = 0; i < cards.length; i++) {
					$('#data-container').append(`
						<div class="card col-4">
							<div class="card-body">
								<h5 class="card-title">${cards[i].flavorText}</h5>
								<h6 class="card-subtitle mb-2 text-muted">${cards[i].subtitle}</h6>
								<h6 class="card-subtitle mb-2">${cards[i].translation}</h6>
								<a href="{{ site.baseurl }}/${cards[i].link}" class="card-link">More</a>
							</div>
						</div>
					`);
				}
			});
		}
	</script>
</body>
</html>
</div>
</div>
<div class="col-sm-1">
</div>

