function addLoader() {
    window.location = window.location.href + "dashboard";
}

$(window).on('load', function() {
    setTimeout(function() {
        addLoader()
    }, 3000);
});