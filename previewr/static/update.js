$(document).ready(function() {
    var updater = {
        socket: null,

        start: function() {
            var url = "ws://" + location.host + "/update";
            updater.socket = new WebSocket(url);

            updater.socket.onmessage = function(event) {
                updater.showMessage(event.data);
            }
        },

        showMessage: function(message) {
            $(".content").html(message)
            $('#toc').toc();
        }
    };
    updater.start();
});