document.addEventListener("submit", sendData);
document.addEventListener("update", getDudes);
function sendData(e) {
    e.preventDefault();
    var name = document.querySelector("#name").value;
    fetch("/create_dude", {
        method: "POST",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name
        })
    })
        .then(function (res) { return res.json(); })
        .then(function (data) {
        var result = data.result;
        document.querySelector("#dude").innerHTML = data["return"];
    })["catch"](function (err) { return console.log(err); });
}
;
function getDudes() {
    fetch("/get_dudes", {
        method: "GET",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json"
        }
    })
        .then(function (res) { return res.json(); })
        .then(function (data) {
        document.querySelector("#dude").innerHTML = '';
        data.forEach(function (element) {
            document.querySelector("#dude").innerHTML += element.character_name + '<br>';
        });
    });
}
setInterval(function () {
    getDudes();
}, 500);
