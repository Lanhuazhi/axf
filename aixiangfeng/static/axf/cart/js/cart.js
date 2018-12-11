
//购物车界面的增加商品的操作
    var price = document.getElementById("price");
    $(function () {
        var addShopping = document.getElementsByClassName("addShopping");
        for (var i = 0;i < addShopping.length; i++) {
            $(addShopping[i]).bind('click',function () {
                var goodsid = this.value;
                $.post("/addgoods/", {"goodsid": goodsid}, function (data) {
                    if (data.status == "200") {
                        var prices = document.getElementById("prices");
                        prices.innerHTML = "共：￥"+data.prices;
                        document.getElementById(goodsid).innerHTML = data.data;
                        document.getElementById(goodsid+"price").innerHTML = "￥"+data.msg;
                    }

                })
            })

        }
    });

//购物车界面的减少购买商品操作
    $(function () {
        var subShopping = document.getElementsByClassName("subShopping");
        //console.log("888888888888888")
        for (var i = 0;i < subShopping.length; i++) {
            //console.log("22222222222222222")
            $(subShopping[i]).bind('click',function () {
                var goodsid = this.value;
                $.post("/subgoods/", {"goodsid": goodsid}, function (data) {
                    if (data.status == "200") {
                        var prices = document.getElementById("prices");
                        prices.innerHTML = "共：￥"+data.prices;
                        document.getElementById(goodsid).innerHTML = data.data;
                        document.getElementById(goodsid+"price").innerHTML = "￥"+data.msg;
                        if (data.data == 0){
                            //购物车减到0时，局部刷新清空不需要的商品
                            var div= document.getElementById(goodsid+"name");
                            div.parentNode.removeChild(div)
                        }
                    }
                })
            })

        }
    });

//是否选择商品下单
   $(function () {
        var group = document.getElementsByClassName("group-img");
        var group1 =document.getElementsByClassName("group-item-checkbox1");
        //onsole.log(group);
        for (var i =0; i < group.length; i++){
            //console.log(i);
            //console.log(group.length);
            //console.log(group[i]);
            $(group[i]).click(function() {
                var groupimg = this.getAttribute("ga");
                $.post("/isselect/",{"groupimg":groupimg},function (data) {
                    if ( data.data == "0") {

                        var prices = document.getElementById("prices");
                        prices.innerHTML = "共：￥"+data.prices;
                        groupimg =document.getElementById(groupimg+"img");
                        groupimg.className="group-item-checkbox1";
                    }
                    if (data.data =="1") {

                        var prices = document.getElementById("prices");
                        prices.innerHTML = "共：￥"+data.prices;
                        groupimg =document.getElementById(groupimg+"img");
                        groupimg.className="group-item-checkbox";
                    }
                })

            })
       }
   }) ;

   //是否全选
    a = 0;
    $(function () {
        //console.log(a)
        var group1 =document.getElementsByClassName("group-item-checkbox2");
        $(group1).click(function () {
            var groupimg = document.getElementsByClassName("group-item-checkbox");
            var groupimg1 = document.getElementsByClassName("group-item-checkbox1");
            $.post("/allselect/",{"a":a},function (data) {
                       if (data.data == "0") {
                           a = 1;
                           var prices = document.getElementById("prices");
                            prices.innerHTML = "共：￥"+data.prices;
                           for (i = 0; i < groupimg.length;) {
                               groupimg[i].className = "group-item-checkbox1";
                           }
                       }
                       if (data.data == "1"){
                           a = 0;
                           var prices = document.getElementById("prices");
                            prices.innerHTML = "共：￥"+data.prices;
                            for (i=0 ;i<groupimg1.length;) {
                                groupimg1[i].className = "group-item-checkbox";
                            }
                        }
                     // groupimg =document.getElementById(groupimg+"img");
                    //$(groupimg).css("background-image","url('/static/axf/cart/img/wait.png')")
            })
        })
    });

    //确认下单
    $(function () {
        var comfirmorder = document.getElementById("goodstime");
        //var index = comfirmorder.selectedIndex;
        // console.log(index)
        // var times =comfirmorder.value;
        // console.log(times)

        $("#group-button").click(function () {
            var times = comfirmorder.value;
            //console.log(times);
            var remarks = $("#remarks").val() ;
            //console.log("进来了888888888888");
            $.post("/comfirmorder/",{"times":times,"remarks":remarks},function (data) {
                if (data.data == "sucess"){
                    alert("成功提交订单，请及时付款")
                    location.href="/cart/";
                }
                if (data.data=="erorr"){
                    alert("请选择商品下单")
                }

            })
        })
    });

