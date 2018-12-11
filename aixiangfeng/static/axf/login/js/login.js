$(document).ready(function () {
    var autocomplete = document.getElementById("autocomplete");
    var accunterr = document.getElementById('accunterr');
    var checker = document.getElementById("checker");
    var password = document.getElementById("password");

    autocomplete.addEventListener("focus",function () {
        checker.style.display = "none"
    },false);

    //验证是否为手机号码
    autocomplete.addEventListener("blur",function () {
        var phonenumber = /^[1][3,4,5,7,8]\d{9}$/;
        instr = this.value;
        if (instr ==""||(!phonenumber.test(instr))){
            checker.style.display = "block";
            return
        }

    },false);
    
    password.addEventListener("focus",function () {
        accunterr.style.display = "none";
    });
    
    password.addEventListener("blur",function () {
        instr1 = this.value;
        if (instr1 ==""){
            accunterr.style.display = "block";
        }
    })

});



//点击验证码弹窗通知
var countdown = 60;
function submit1(obj) {
        var userpthon = $("input[name=phone]") ;
        var phones = $.trim(userpthon.val());
        if (phones == "") {
            alert("请输入正确的手机号码");
            return
        }
        if (countdown == 0){
            obj.removeAttribute("disabled");
            obj.value = "重新获取验证码";
            countdown = 60;
            return
        }
        else{
            obj.setAttribute("disabled",true);
            obj.value = "重新发送("+countdown+"S)";
            countdown--;
        }
        setTimeout(function () {
        submit1(obj)
         },1000);

}

$(function () {
    $('#login-send').click(function () {
        var code = $("input[name=password]");
        var accunterr = document.getElementById('accunterr');
        $.ajax({
            cache: false,
            type: 'POST',
            url: '/send/',
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}',
                'phones': $("#autocomplete").val()
            },
            async: true,
            success: function (data) {
                alert(data.data);

            }
        })

    })
});


$(function () {
    $("#submit2").click(function () {
        $.ajax({
            cache:false,
            type: "POST",
            url:"/login/",
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}',
                'phones':$("#autocomplete").val(),
                'code':$("#password").val(),
            },
            async: true,
            success:function (data) {
                if (data.msg == "ok"){
                    location.href="http://lruqiao.top:8000"
                }
                else {
                    alert(data.msg);
                }
            }
        })
    })

});



