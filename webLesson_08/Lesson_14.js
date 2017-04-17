function validateU() {
    var x = document.forms.input.username.value;
    var atPos = x.indexOf("@");
    var dotPos = x.lastIndexOf(".");
    var y =  (document.forms.input.password.value).length;

        if (atPos < 1 || dotPos < atPos + 2 || dotPos + 2 > x.length && y < 6)
            alert("Both password and username are incorrect!!")
        else
            if (atPos < 1 || dotPos < atPos + 2 || dotPos + 2 > x.length)
                 alert("This is not a valid email address!");
            else if (y < 6)
                alert("Password is incorrect");
                    else
                        alert("Success!!!!")


}