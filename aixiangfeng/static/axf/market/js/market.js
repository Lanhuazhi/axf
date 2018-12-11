$(function () {

    $("#all_types").click(function () {

        $("#all_types_container").show();
        $("#all_type_logo").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
        $("#sort_container").hide();
        $("#sort_rule_logo").addClass("glyphicon-chevron-up").removeClass("glyphicon-chevron-down");
    });


    $("#all_types_container").click(function () {
        $(this).hide();
        $("#all_type_logo").addClass("glyphicon-chevron-up").removeClass("glyphicon-chevron-down");

    });


    $("#sort_rule").click(function () {
        $("#sort_container").show();
        $("#sort_rule_logo").addClass("glyphicon-chevron-down").removeClass("glyphicon-chevron-up");
        $("#all_types_container").hide();
        $("#all_type_logo").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
    });

    $("#sort_container").click(function () {
        $(this).hide();
        $("#sort_rule_logo").addClass("glyphicon-chevron-up").removeClass("glyphicon-chevron-down");
    });
})
    // $("#all_types_container>div>a").click(function () {
    //     $('#all_types').find("span").text(($(this).find("span").text()))
    // })
    // $("#all_types_container>div>a").each(function () {
    //     $(this).click(function (e) {
    //         var typeid = $('#market').attr('name')
    //         var childtypeid = $(this).prop('name')
    //         urlStr = '/axf/childtype/?typeid='+typeid+'&childtypeid='+childtypeid
    //         $.ajax({
    //             type:"get",
    //             url:urlStr,
    //             async:true,
    //             dateType:'json',
    //             success:function(obj){
    //             }
    //         })
    //     })
    // })
    //
    // $("#sort_container>div>a").click(function () {
    //     var typeid = $('#market').attr('name')
    //     urlStr = '/axf/order/order='+$(this).attr('name')
    //     $.ajax({
    //         type:"get",
    //         url:urlStr,
    //         async:true,
    //         dateType:'json',
    //         success:function(obj){
    //         }
    //     })
    // })

//    添加商品到购物车
//     var addShopping = document.getElementsByClassName("addShopping");
//     var subShopping = document.getElementsByClassName("subShopping");
//     console.log('**************/////////')
//
//     for (var i = 0; i<addShopping.length; i++) {
//         console.log('*********************')
//         addShopping = addShopping[i];
//         console.log('********************')
//
//         addShopping.click( function () {
//             console.log('2222222222222222222222')
//             var goodsid = this.getAttribute("ga");
//             $.post("/addgoods/", {"goodsid": goodsid}, function (data) {
//                 if (data.status == "901") {
//                     window.open("/login/");
//                 }
//                 if (data.status == "200") {
//                     document.getElementsByClassName(goodsid).innerHTML = data.data
//                 }
//             })
//         })
//     }
// //
//     for (var i=0; i<subShopping.length; i++) {
//         subShopping = subShopping[i];
//         subShopping.addEventListener("click",function () {
//             var goodsid = this.getAttribute("value");
//             $.post("/addgoods/",{"goodsid":goodsid},function (data) {
//                 if (data.status == "901") {
//                     window.open("/login/");
//                 }
//                 if (data.status =="200"){
//                     document.getElementById(goodsid).innerHTML = data.data
//                 }
//             })
//         })

//



    var price = document.getElementById("price");
    $(function () {
        var addShopping = document.getElementsByClassName("addShopping");
        for (var i = 0;i < addShopping.length; i++) {
            $(addShopping[i]).bind('click',function () {
                var goodsid = this.value;
                $.post("/addgoods/", {"goodsid": goodsid}, function (data) {
                    if (data.status == "901") {
                        window.open("/login/", target = "_self");
                    }
                    if (data.status == "200") {
                        document.getElementById(goodsid).innerHTML = data.data;
                        if (data.data == 0){
                            console.log("88888888888888888888");
                            var span = document.getElementById(goodsid+"span");
                            span.parentNode.removeChild(span)
                        }
                    }
                    if (data.status == "error") {
                        alert(data.msg)
                    }
                })
            })

        }
    });


        $(function () {
        var subShopping = document.getElementsByClassName("subShopping");
        for (var i = 0;i < subShopping.length; i++) {
            $(subShopping[i]).bind('click',function () {
                var goodsid = this.value;
                $.post("/subgoods/", {"goodsid": goodsid}, function (data) {
                    if (data.status == "901") {
                        window.open("/login/", target = "_self");
                    }
                    if (data.status == "200") {
                        document.getElementById(goodsid).innerHTML = data.data;
                    }
                })
            })

        }
    });





//     // 添加商品到购物车
//   $("#subShopping").click(function () {
//         //    拿到商品id发送给服务器
//         var goodsid = this.value
//         // console.log(goodsid);
//         // console.log($(this).attr("class"));
//         // console.log("**************")
//         // var goodsid2 = $(this).prop("goodsid");
//         // console.log(goodsid2);
//         // console.log($(this).prop("class"));
//
//         $.post("/addgoods/", {"goodsid": goodsid}, function (data) {
//
//             if (data.status == "901") {
//                 window.open("/login/", target = "_self");
//             } else if (data["status"] == "200") {
//                 var g_num = data["g_num"];
//                 var span_num = subShop.next();
//                 span_num.html(g_num);
//             } else if (data["status"] == "902") {
//                 alert(data["msg"]);
//             }
//         })
//     })
//
//
// })