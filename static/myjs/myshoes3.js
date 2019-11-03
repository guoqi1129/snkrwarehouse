
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
                    {title:'快递费用',data:'ship_inter_info__ship_rmb'},
                    {title:'价格(rmb)',data:'buy_info__final_rmb'},

                    {title:'开始时间',data:null,
                        render: function(data,type,row,meta){
                            var a="";
                            if(data.status=="国内卖出"){a = data.time5}
                            else {a = data.time6}
                            return a
                        }},
                    {title:'状态',data:'status'},
                    {title:'备注',data:'goods__remark'},
                    {title:'操作',data:null,
                        render: function(data,type,row,meta){
                            if(data.status=="国内卖出"){btncss='btn-primary';btnaction='name="ship"';btntext="<i class=\"fa fa-fw  fa-money\"></i>到账";}
                            else{btncss='btn-warning';btnaction='name="look"';btntext="<i class=\"fa fa-fw fa-info\"></i>查看";}
                            return '<button type="button" class="btn btn-sm '+ btncss+'" id="'+meta.row +'" '+ btnaction + '>'+ btntext +'</button>';
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
            $('#'+data[i].id).click(function () {
                if($(this).attr("name")=='ship'){//收货
                    $.post("shiptochina",{id:$(this).attr('id'),
                            csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"]').val(),
                            action:'ship_to_china'},
                        function (data,state) {
                            get_response_data(data,state);
                        },
                        'json');}

                else{
                    lookgoods($(this).attr("id"))
                }
            });
        }
    }

});