$('#get-data'). click(() => {
    var url = "/data/languages.json";
    $.getJSON(url, function (data) {
        var slag = JSON.parse(data).filter(doc => doc.name === 'English');
        console.log(slag);
    });
})