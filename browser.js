$(document).ready(function(){
    var targets = $('.filter'),
    buttons = $('.filter-button');
    var data = $.getJSON("data/publications.json");
    buttons.click(function(){
        var value = $(this).data('filter');
        if(value == "all")
        {
            buttons.removeClass('checked');
            targets.show();
        }
        else
        {
            if($(this).hasClass('checked'))
            {
                $(this).removeClass('checked');
                var checkedClasses = buttons.filter('.checked').toArray().map(function(btn){return $(btn).data('filter');});
                if(checkedClasses.length == 0)
                {
                    buttons.removeClass('checked');
                    targets.show();
                }
                else
                {
                    checkedClasses = $.grep(checkedClasses, function(n, i){ return n != value }),
                    selector = '.' + checkedClasses.join('.'),
                    show = targets.filter(selector);
                    targets.not(show).hide();
                    show.show();
                }
            }
            else
            {
                $(this).addClass('checked');
                var checkedClasses = buttons.filter('.checked').toArray().map(function(btn){return $(btn).data('filter');}),
                selector = '.' + checkedClasses.join('.'),
                show = targets.filter(selector);
                targets.not(show).hide();
                show.show();

            }
        }
});
