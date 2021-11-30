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

function resetResults() {
    var text = document.getElementById("results").innerHTML = "";
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

function hideInput() {
    var check = document.getElementById("message-box");
    check.classList.add("dont-show");
    var check2 = document.getElementById("homomorphic-choices");
    check2.classList.remove("dont-show");
    var check3 = document.getElementById("homomorphic-choices-2");
    check3.classList.remove("dont-show");
}

function showInput() {
    var check = document.getElementById("message-box");
    check.classList.remove("dont-show");
    var check2 = document.getElementById("homomorphic-choices");
    check2.classList.add("dont-show");
    var check3 = document.getElementById("homomorphic-choices-2");
    check3.classList.add("dont-show");
}

function toggle() {
    var choice = document.getElementById("method-type");
    if (choice.value == "Homomorphic Encryption") {
        //console.log("homomorphic");
        hideInput();
    }
    else {
        //console.log("not homomorphic");
        showInput();
    }
}

toggle(); //do not remove because we need to run toggle() when page loads

