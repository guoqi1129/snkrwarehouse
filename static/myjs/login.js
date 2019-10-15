$(function () {
    var csrftoken = $.cookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    $("#logins").click(function () {
        if ($("#username").val().length == 0){
            $("#inform").text("用户名不能为空");
        }else if ($("#password").val().length == 0) {
            $("#inform").text("密码不能为空");
        }else if ($("#username").val().length != 0 && $("#password").val().length != 0){
            if(/(^[1-9]\d*$)/.test($("#username").val())){
                $("#inform").text("用户名含有非法字符");
            }else {
                var url = "login";
                var data = {
                    "name": $("#username").val(),
                    "pwd": $("#password").val(),
                };

                $.ajax({
                    url: url,
                    type: "POST",
                    data: data,
                    success:function (arg) {
                        alert(arg);
                    }
                })
            }
        }

    });
});