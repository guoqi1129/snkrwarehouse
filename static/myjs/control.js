$(function () {
$("#newFormSub").click(function () {
    $("#newSKUform").ajaxForm(function (data) {
        console.log(data);
    });
});
    $('.select2').select2({
        tags:true
    })
});
