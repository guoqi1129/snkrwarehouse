
$(function () {
    operatedata = [];
    operateindex = 0;
    getmyshoetable();
    function getmyshoetable(){
        $.get('myShoeTable',function (data,status) {
            make_table(data);
        });
    }
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
                {title:'尺码',data:'size'},
                {title:'购买日期',data:null,
                render: function(data,type,row,meta){
                    return data.operatortime.substring(0,10);
                }},
                {title:'状态',data:'warehouse__status'},
                {title:'价格($)',data:'final_price'},
                {title:'价格(rmb)',data:'final_rmb'},
                {title:'操作',data:null,
                render: function(data,type,row,meta){
                    if(data.warehouse__status=="已入库"){btncss='btn-primary';btnaction='name="ship"';btntext="<i class=\"fa fa-fw fa-plane\"></i>发货";}else{btncss='btn-warning';btnaction='name="look"';btntext="<i class=\"fa fa-fw fa-info\"></i>查看";}
                    return '<button type="button" class="btn btn-sm '+ btncss+'" data-toggle="modal" data-target="#modal-default" id="'+meta.row +'" '+ btnaction + '>'+ btntext +'</button>';
                }}

            ],
                pageLength:5,
            "order":[[6,'desc']],
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
        for(var i=0;i<data.length;i++){
            $('#example1').delegate("#"+(i),"click",[],
                function () {
                    if($(this).attr("name")=='ship'){
                        shipgoods($(this).attr("id"));}
                    else{lookgoods($(this).attr("id"));}
                }
                );

            //
            // $('#'+(i+1)).click(function () {
            //     if($(this).attr("name")=='ship'){
            //     shipgoods($(this).attr("id"));}
            //     else{lookgoods($(this).attr("id"));}
            // });
        }
    }

});