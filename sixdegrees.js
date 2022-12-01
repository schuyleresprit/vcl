
			<script language="javascript">
			newlink = document.getElementById("Author");
			newlink.addEventListener('submit', event => {
				event.preventDefault();
				submitdata = {
					"ajax": 1,
				"Author": "",
				"Pubdate": "",
				"Publisher": "",
				"Publocation": "",
				"Title": "",
				};
				$.ajax({
					type: "Author",
					url: "publications.json",
					data: submitdata,
					dataType: "html",
					success: function( data ) {
						document.getElementById("Author").innerHTML = data;
					}
				});
			});
			</script>
