$(function () {
$("#newFormSub").click(function () {
    $("#newSKUform").ajaxForm(function (data) {
        console.log(data);
    });
});
});
