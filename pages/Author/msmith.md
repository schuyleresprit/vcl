---
layout: defaultau
title: "Michael Smith"
authorId: msmith
permalink: /msmith/
---
{% include loadAuthor.html %}
<script>
    $(document).ready(function(){
        showAuthorBio('{{ page.authorId }}');
   });
</script>