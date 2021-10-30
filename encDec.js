function hideDEC() {
    var check = document.getElementById("decryption");
    check.classList.add("dont-show");
    var check2 = document.getElementById("encryption");
    check2.classList.remove("dont-show");
    //console.log("hideDEC+showENC");
}

function hideENC() {
    var check = document.getElementById("encryption");
    check.classList.add("dont-show");
    var check2 = document.getElementById("decryption");
    check2.classList.remove("dont-show");
    //console.log("hideENC+showDEC");
}

function check() {
    if (document.getElementById("gen-select-button").checked) { //remember gen-select-button is unchecked by default when page loads
        hideENC();
    } else {
        hideDEC();
    }
}

check(); //do not remove because we need to run check() when page loads