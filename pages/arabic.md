---
layout: default
title: Arabic
permalink: /arabic
---
<div class="individual_language">
<div class="page_title"><h3> Arabic</h3></div>

Represented here are the authors who have written works in Arabic. Some of these may be texts translated into Arabic from other languages.

<html>
<body>
	<div class="container">
		<div class="input-group mb-3">
			<input id="search-box" type="text" class="form-control" placeholder="Search for a an author">
		</div>
		<div id="data-container" class="row">
		</div>
	</div>
	<script>
		let datasets = [
			{
				"type" : "arabic",
				"url" : "/data/arabic.json"
			}
		];
		var dataLinks = [];
		$( document ).ready(function() {
			for (i = 0; i < datasets.length; i++) {
				dataLinks.push({
					"type" : datasets[i].type,
					"data" : siftData(datasets[i].url, datasets[i].type)
				});
			}
			//Set triggers
			$('#search-box').on('input', function (event) {
				showCategory(event.target.value);
			})
			//Populate page
			setTimeout(showCategory, 1000);
		});
		function siftData (url, dataType) {
			var temp = [];
			$.getJSON(url, function (data) {
				switch (dataType) {
					case "arabic":
						for (key in data) {
							temp.push({
								"flavorText" : key,
								"link" : key,
							});
						}
						break;
					default:
						break;
				}
			});
			return temp;
		}
		function showCategory (filter = "") {
			$('#data-container').html('');
			filter = filter.trim();
			dataLinks.forEach(element => {
				if ((filter == "") && element.data.length > 0) {
					for (i = 0; i < element.data.length; i++) {
						$('#data-container').append(`
							<div class="card col-4">
								<div class="card-body">
									<h5 class="card-title">${element.data[i].flavorText}</h5>
									<h6 class="card-subtitle mb-2 text-muted">${element.type}</h6>
									<a href="/${element.data[i].link}" class="card-link">More</a>
								</div>
							</div>
						`);
					}
				} else {
					for (i = 0; i < element.data.length; i++) {
						if (element.data[i].flavorText.toLowerCase().includes(filter.toLowerCase()))
							$('#data-container').append(`
								<div class="card col-4">
									<div class="card-body">
										<h5 class="card-title">${element.data[i].flavorText}</h5>
										<h6 class="card-subtitle mb-2 text-muted">${element.type}</h6>
										<a href="/${element.data[i].link}" class="card-link">More</a>
									</div>
								</div>
							`);
					}
				}
			});
		}
	</script>
</body>
</html>
</div>
