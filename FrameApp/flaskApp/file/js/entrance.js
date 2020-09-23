function input_submit() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var p_receive = document.getElementById("p_receive");
    if (username == "" || username == null || password == "" || password == null){
        p_receive.innerHTML = "User or pass cannot be empty!";
    }else {
        p_receive.innerHTML = "Verifying login information...";
        $.ajax({
            url : "/rain",
            cache : false,
            type : 'POST',
            data : {
                "username": username,
                "password": password
            },
            success : function(data) {
                var obj = eval("("+data+")");
                if(obj.success==true) {
                    p_receive.innerHTML = "Logging in...";
                    $("#input_entergoin").val(obj.token);
                    $("#form_entergoin").attr("action","/rainentergoin");
                    $("#form_entergoin").submit();
                }else if(!obj.success) {
                    p_receive.innerHTML = "User does not exist or the pass is incorrect!";
                }
            },
            error : function(error) {
                p_receive.innerHTML = "Unknown exception about" + error + "!";
            }
        });
    }
}

