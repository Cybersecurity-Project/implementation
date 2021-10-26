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

console.log(document.getElementById("gen-select-button").checked)

let submit = document.querySelector(".generateButton");
//shows message when generates message
submit.addEventListener('click', (e) => {
    $("p").text("resultMessage").show(); 
    let x = document.getElementById("resultMessage").textContent;
    console.log(x);
    e.preventDefault();
});

function showMsg(e) {
    $("p").text("resultMessage").show(); 
    e.preventDefault();
}

//runs function on page load
function hideMsg() {
    // let x = document.getElementById("resultMessage").textContent;
    $("p").text("resultMessage").hide(); 
}

window.onload = hideMsg;
