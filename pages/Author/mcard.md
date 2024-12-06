---
layout: defaultau
title: "Maisy Card"
authorId: mcard
permalink: /mcard/
---
{% include loadAuthor.html %}
<script>
    $(document).ready(function(){
        showAuthorBio('{{ page.authorId }}');
   });
</script>