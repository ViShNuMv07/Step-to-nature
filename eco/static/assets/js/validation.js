function validation() {
    var a = document.getElementById("name").value;
    if (a.length == 0) {
        alert("Name must be filled");
        return false;
    }

    var b = document.getElementById("mob_no").value;
    if (b.length != 10 || isNaN(b)) {
        alert("Mobile Number must be 10 digits");
        return false;
    }

    // Correcting the regex and removing the quotes around it
    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_{|}~-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,7}$/;
    var c = document.getElementById("email").value;
    if (!c.match(validRegex)) {
        alert("Please Enter a valid Email Address");
        return false;
    }

    var d = document.getElementById("dob").value;
    if (d.length == 0) {
        alert("Date of birth must be filled");
        return false;
    }

    var e = document.getElementById("username").value;
    if (e.length == 0) {
        alert("Username must be filled");
        return false;
    }

    var f = document.getElementById("password").value;
    // Correcting the condition for password length
    if (f.length < 8 || f.length > 16) {
        alert("Password must be between 8 and 16 characters");
        return false;
    }

    // If all checks pass
    return true;
}
