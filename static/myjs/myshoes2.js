
$(function () {
    operatedata = [];
    operateindex = 0;
    $.get('myShoeTable',function (data,status) {
        make_table(data);
    });

    function shipgoods(id) {
        $('#id_id').val(operatedata[id].id);
        $('#id_buy_date').val(operatedata[id].operatortime.substring(0,10));
        $('#id_name').val(operatedata[id].goods__name);
        $('#id_sku').val(operatedata[id].goods__sku);
        $('#id_size').val(operatedata[id].size);
    }
    function lookgoods(id) {
        $.ajax({
            type:"POST",
                dataType:"json",
                url:"/table/showGoodsDetail",
                data:{'id':id},
            complete:function(){
            location.href ="/table/showGoodsDetail"}
        })
    }

    $('.select2').select2({
        tags: true
    });
    function make_table(data) {
        $('#example1').empty();
        operatedata = data;
        $('#example1').DataTable(

            {data:data,
            columns:[
                {title:'目类',data:'goods__category'},
                {title:'品牌',data:'goods__brand'},
                {title:'款式',data:'goods__styles'},
                {title:'商品名称',data:'goods__name'},
                {title:'商品编码',data:'goods__sku'},
                {title:'尺码',data:'buy_info__size'},
                {title:'购买日期',data:null,
                render: function(data,type,row,meta){
                    return data.buy_info__operatortime.substring(0,10);
                }},
                {title:'快递公司',data:'ship_inter_info__ship_store'},
                {title:'快递单号',data:'ship_inter_info__ship_number'},
                {title:'快递费用',data:'ship_inter_info__ship_rmb'},
                {title:'开始时间',data:null,
                    render: function(data,type,row,meta){
                        var a="";
                        if(data.status=="回国中"){a = data.time2}
                        else if(data.status=="国内入库"){a = data.time3}
                        else if(data.status=="国内上架"){a = data.time4}
                        else if(data.status=="国内卖出"){a = data.time5}
                        return a
                    }},
                {title:'状态',data:'status'},
                {title:'价格(rmb)',data:'buy_info__final_rmb'},
                {title:'备注',data:'goods__remark'},
                {title:'操作',data:null,
                render: function(data,type,row,meta){
                    if(data.status=="回国中"){btncss='btn-primary';btnaction='name="ship"';btntext="<i class=\"fa fa-fw  fa-get-pocket\"></i>收货";}
                    else if(data.status=="国内入库"){btncss='btn-success';btnaction='name="up"';btntext="<i class=\"fa fa-fw fa-bullhorn\"></i>上架";}
                    else if(data.status=="国内上架"){btncss='btn-info';btnaction='name="sell"';btntext="<i class=\"fa fa-fw fa-balance-scale\"></i>售出";}
                    else{btncss='btn-warning';btnaction='name="look"';btntext="<i class=\"fa fa-fw fa-info\"></i>查看";}
                    return '<button type="button" class="btn btn-sm '+ btncss+'" id="'+data.id +'" '+ btnaction + '>'+ btntext +'</button>';
                }}

            ],
            "order":[[6,'desc']],
                bStateSave: true,
                "oLanguage": {
                    "sLengthMenu": "每页显示 _MENU_ 条记录",
                    "sZeroRecords": "对不起，查询不到任何相关数据",
                    "sInfo": "当前显示 _START_ 到 _END_ 条，共 _TOTAL_条记录",
                    "sInfoEmtpy": "找不到相关数据",
                    "sInfoFiltered": "数据表中共为 _MAX_ 条记录)",
                    "sProcessing": "正在加载中...",
                    "sSearch": "搜索",
                    "oPaginate": {
                        "sFirst": "第一页",
                        "sPrevious":" 上一页 ",
                        "sNext": " 下一页 ",
                        "sLast": " 最后一页 "
                    },
                }

            });
        function get_response_data(data,state) {
            console.log(data);
            window.location.reload();
        }

        function lookgoods(id) {
            $.ajax({
                type:"POST",
                dataType:"json",
                url:"/table/showGoodsDetail",
                data:{'id':id},
                complete:function(){
                    location.href ="/table/showGoodsDetail"}
            })
        }

        for(var i=0;i<data.length;i++){
            $('#example1').delegate("#"+data[i].id,"click",[],
                function () {
                if($(this).attr("name")=='ship'){//收货
                    $.post("shiptochina",{id:$(this).attr('id'),
                        csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"]').val(),
                        action:'ship_to_china'},
                        function (data,state) {
                        get_response_data(data,state);
                        },
                        'json');}
                else if($(this).attr("name")=='up'){
                    $.post("shiptochina",{id:$(this).attr('id'),
                        csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"]').val(),
                        action:'ready_to_sell'},
                        function (data,state) {
                        console.log(data);
                            get_response_data(data,state);
                        },'json');
                    }
                else if($(this).attr("name")=='sell'){
                    $.post("shiptochina",{id:$(this).attr('id'),
                            csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"]').val(),
                            action:'selled'},
                        function (data,state) {
                            console.log(data);
                            get_response_data(data,state);
                        },'json');
                }
                else{
                    lookgoods($(this).attr("id"))
                }
            });
        }
    }

});