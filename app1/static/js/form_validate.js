$(document).ready(function () {

    $('#errmob').hide();
    $('#errpass1').hide();



    var errmob = true;
    var errpass1 = true;


    $('#id_phone').keyup(function () {
        mobno_check();
    });
    function mobno_check() {
        var id_phone = $('#id_phone').val();
        if (id_phone.length == ""){
            $('#errmob').show();
            $('#errmob').html('. Please Fill The User Mobno');
            $('#errmob').focus();
            errmob = false;
            return false;
        }else if((id_phone.length != 10) || (isNaN(id_phone))){
            $('#errmob').show();
            $('#errmob').html('. Mobile number must be 10 degits not Char');
            $('#errmob').focus();
            errmob = false;
            return false;
        }else {
            $('#errmob').hide();
        }
    }



    $('#id_password').keyup(function () {
        pass1_check();
    });
    function pass1_check() {
        var id_password = $('#id_password').val();
        var p_patern = /^(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,15}$/;
        if (id_password.length == ""){
            $('#errpass1').show();
            $('#errpass1').html('. Please Fill The Password');
            $('#errpass1').focus();
            errpass1 = false;
            return false;
        }else if(!id_password.match(p_patern)){
            $('#errpass1').show();
            $('#errpass1').html('. password minimum six characters.<br>. password at least one lowercase letter.<br>. password contains one number.<br>. password contains one special character:');
            $('#errpass1').focus();
            errpass1 = false;
            return false;
        }else {
            $('#errpass1').hide();
        }
    }

    $("#btn-submit").click(function () {

        var errmob = true;
        var errpass1 = true;

        mobno_check();
        pass1_check();
        if ((errmob==true) && (errpass1==true)){
            return true;
        }else {
            return false;
        }
    })
});