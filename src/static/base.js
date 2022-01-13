"use strict";
document.addEventListener("submit", sendData);
document.addEventListener("update", getDudes);
const socket = io.connect('localhost:5000');
socket.on('connect', function () {
    socket.send('User connected');
});
socket.on('message', function (msg) {
    getDudes(msg);
});
function sendData(e) {
    e.preventDefault();
    const name = document.querySelector("#name").value;
    fetch("/create_dude", {
        method: "POST",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name,
        })
    })
        .then(socket.send('new character'))
        .catch(err => console.log(err));
}
;
function getDudes(dudes) {
    let work = JSON.parse(dudes);
    document.querySelector("#dude").innerHTML = '';
    Object.entries(work).forEach(element => {
        let char = element[1];
        document.querySelector("#dude").innerHTML += char.character_name + '       level: ' + char.character_level + '<br>';
    });
}
