---
layout: default
title: English
permalink: /English
---

<html>
<body>
	<div class="container">
		<div class="input-group mb-3">
			<input id="search-box" type="text" class="form-control" placeholder="Search for an author">
		</div>
     </div>
		<div id="data-container" class="row">
	    </div>
	<script>
		let datasets = [
			{
				"type" : "languages",
				"url" : "/data/languages.json"
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
			json.getKeys (obj) 
    		const key = Object.key(obj);
    		for (let i = 0; i < keys.length; i++){
     		   const key = key[i];
        		if (typeof obj[key] === 'English') {
        		 key.splice(i+1, 0, getKeys(obj[key]));
        		    i++;
        		}
    }
			});
    return key;
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
