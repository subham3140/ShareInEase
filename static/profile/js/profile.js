function refreshPage() {
    window.location.reload()
}

$('.createqr').on("click", () => {
    $('.main-content .container').css("opacity", "0.3")
    $('#loader-wrapper').removeAttr("hidden")
    let csrf_token = $("input[name=csrfmiddlewaretoken]").val()
    let id = $(".createqr")[0].value
    $.ajax({
        url: "/shareApp/createqr/",
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token
        },
        data: { "id": id },
        success: function(response) {
            if (response["result"] == "ok") {
                setTimeout(function() {
                    refreshPage()
                }, 3000);
            }
        }
    })
})

function donedownload() {
    $('#loader-wrapper').attr("hidden", "true")
    $('.d').css("opacity", "1")
    swal({
        title: "Download Successful",
        icon: "success",
        buttons: { ok: { text: "OK", className: "btn btn-info" } }
    });
}

$('.bdownload').on("click", () => {
    $('.d').css("opacity", "0.3")
    $('#loader-wrapper').removeAttr("hidden")
    setTimeout(function() {
        donedownload()
    }, 4000);
})