
			<script language="javascript">
			newlink = document.getElementById("Author");
			newlink.addEventListener('submit', event => {
				event.preventDefault();
				submitdata = {
					"ajax": 1,
				"a": "",
				"b": "",
				"use_role_types": "",
				"rt0": "",
				"company": "",
				};
				$.ajax({
					type: "POST",
					url: "publications.json",
					data: submitdata,
					dataType: "html",
					success: function( data ) {
						document.getElementById("linkresult").innerHTML = data;
					}
				});
			});
			</script>
