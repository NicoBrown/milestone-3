$(document).ready(function () {
    $(".sidenav").sidenav({
        edge: "right"
    });
    $('.parallax').parallax();
    $(".collapsible").collapsible();
    $('input').characterCounter();
    $('.fixed-action-btn').floatingActionButton()
    $('.datepicker').datepicker();

});

window.setTimeout(function () {
    $("#flash").fadeTo(500, 0)
}, 4000);