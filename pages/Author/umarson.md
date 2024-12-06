---
layout: defaultau
title: "Una Marson"
authorId: umarson
permalink: /umarson/
---
{% include loadAuthor.html %}
<script>
    $(document).ready(function(){
        showAuthorBio('{{ page.authorId }}');
   });
</script>