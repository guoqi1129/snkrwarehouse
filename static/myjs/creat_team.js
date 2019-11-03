$(function () {
    var subFormNum=1;
    formcontrol = $(".add-sub-form");
    $('.plus-user').click(function () {
        if(subFormNum < 8){
        formcontrol.append(
            "<div class=\"subform"+ (subFormNum+1) +"\">\n" +
            "<div class=\"col-md-6\">\n" +
            "<label for=\"id_form-"+subFormNum+"-username\">用户名:</label> <input type=\"text\" name=\"form-"+subFormNum+"-username\" class=\"form-control\" id=\"id_form-"+subFormNum+"-username\" required>\n" +
            "</div><div class=\"col-md-6\">\n" +
            "<label for=\"id_form-"+subFormNum+"-percentage\">所占比例(100以内数字):</label> <input type=\"text\" name=\"form-"+subFormNum+"-percentage\" class=\"form-control\" id=\"id_form-"+subFormNum+"-percentage\" required>\n" +
            "</div>\n" +
            "</div>"
        );
        subFormNum = subFormNum+1;}
    });
    $('.minus-user').click(function () {
        if(subFormNum!=1){
            $(".subform"+subFormNum).empty();
            subFormNum = subFormNum -1;
        }
    });
});