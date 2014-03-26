(function ($) {
    "use strict";
    var date = 0;
    var timerId = setInterval(function () {
        $.ajax({
            url: "last_refresh.json",
            dataType: "json"
        }).done(function (data) {
            if (date !== 0 && date !== data.date){
                window.location.reload(true)
            }
            date = data.date

        }).fail(function () {
            var err = $("<div></div>").
                addClass('alert').
                addClass('alert-danger').
                html('Connection to server lost!')
            $('.container').prepend(err);
            clearTimeout(timerId)
        });
    }, 1000);

})($);