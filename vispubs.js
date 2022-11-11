(function listpublishers(){
    this.init =function() {
        this.search();
    };

/* --------------------------
        SEARCH START
--------------------------- */
    this.search = function(){
        var form = document.querySelector('#form');
        form.addEventListener('submit', function(e){
            e.preventDefault();
            var searchValue = document.querySelector('#input_search').value;

            form.reset();
            getData(searchValue.split(' ').join('+'));

        });
    };

/* --------------------------
        SEARCH END
--------------------------- */

/* --------------------------
        GET DATA START
--------------------------- */
    this.getData = function(publisher) {

        var http = new XMLHttpRequest();
        var url = 'data/publications.json';
        var method = 'GET';
        var container = document.querySelector('#publisher_container');

        container.innerHTML = '';
        http.open(method, url);

        http.onreadystatechange = function(){
            if(http.readyState === XMLHttpRequest.DONE && http.status === 200) {

                var jsonResponse = JSON.parse(http.response);

                showArtist(jsonResponse);

            }else if(http.readyState === XMLHttpRequest.DONE && http.status !== 200) {
                document.querySelector('#no_data').style.display = 'none';
                document.querySelector('#something_wrong').style.display = 'block';
            }
        }

        http.send();
    };
/* --------------------------
        GET DATA END
--------------------------- */

/* --------------------------
    SHOW ARTIST START
--------------------------- */
    this.showTitle = function(object) {
        var container = document.querySelector('#title_container');
        var template = '';

        if(object.results.length > 0) {

            document.querySelector('#something_wrong').style.display = 'none';
            document.querySelector('#no_data').style.display = 'none';

            for(var i = 0; i < object.results.length; i++) {
                template += '<div class="col-sm-3 title_item">';
                template +=     '<div class="item_thumbnail" style="background:url('+ object.results[i].artworkUrl100+')"></div>';
                template +=     '<div class="item_title">'+object.results[i].collectionName+'</div>';
                template +=     '<div class="item_price">';
                template +=         '<span>Price:</span> '+object.results[i].collectionPrice;
                template +=     '</div>';
                template +=     '<a href="'+object.results[i].collectionViewUrl+'" target="_blank">Buy Now</a>';
                template += '</div>';
            }

            container.innerHTML = '';
            container.insertAdjacentHTML('afterbegin', template);

        }else {
            document.querySelector('#something_wrong').style.display = 'none';
            document.querySelector('#no_data').style.display = 'block';
        }
    };

/* --------------------------
    SHOW ARTIST END
--------------------------- */

    this.init();
})();
