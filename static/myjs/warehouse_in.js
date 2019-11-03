$(function () {
    var search_rlt=[];
    $('.select2').select2({
        tags: true
    });
    search_result = $('.search-result');
    search_result.hide();
    search_input = $('.search-input');
    $('.search').click(function () {
        if(search_input.val()==""){
            search_input.attr("placeholder","请输入有效的内容");
        }else{
            $.post("search",
                {searchs:search_input.val(),
                    csrfmiddlewaretoken:$("input[name='csrfmiddlewaretoken']").val()},
                function (data,status) {
                if(data.length ==1 & data[0].error){}else{
                    search_result.empty();
                    search_rlt = data;
                    for(var i=0;i<data.length;i++){
                        describe = data[i].category + "/" + data[i].styles + "/" + data[i].brand + "/" + data[i].name + "/" + data[i].sku;
                        search_result.append("<option value='" +i+ "'>" + describe + "</option>");
                }}


            },"json")
        }
        search_result.show();
    });
    search_result.change(function(){
        temp = search_rlt[parseInt($(this).val())];
        $("#id_category").val(temp.category);
        $("#id_brand").val(temp.brand).trigger('change');
        $("#id_styles").val(temp.styles);
        $("#id_name").val(temp.name);
        $("#id_sku").val(temp.sku);
    });
    sizes = $("#id_size");
    sizes.val('123');
    ori_price = $("#id_ori_price");
    exchange = $("#id_exchange");
    fees = $("#id_fees");
    taxes = $("#id_taxes");
    final_price = $('#final-price');
    ori_price.bind('input propertychange',function(){cal_final_price()});
    exchange.bind('input propertychange',function(){cal_final_price()});
    fees.bind('input propertychange',function(){cal_final_price()});
    taxes.bind('input propertychange',function(){cal_final_price()});
    function cal_final_price() {
        if(isNaN(parseFloat(ori_price.val()))||isNaN(parseFloat(exchange.val()))||isNaN(parseFloat(taxes.val()))||isNaN(parseFloat(fees.val()))){
            final_price.html("");
        }else{
            final_price.html("最终价格："+(Math.round(parseFloat((ori_price.val())*(1+parseFloat(taxes.val())/100)+parseFloat(fees.val()))*parseFloat(exchange.val())*100)/100).toString()+"元");
        }
    }
    $('#datepicker').datepicker({
        autoclose: true,
        format:'yyyy-mm-dd',
    });


});