'use strict';
document.addEventListener("submit", sendData);
document.addEventListener("update", getDudes);

///<reference path="socket.io.js"/>
const socket = io.connect('');

const app = new PIXI.Application();

socket.on('connect',function() {
    socket.send('User connected')
})

socket.on('message',function(msg: typeof event){
    getDudes(msg);
})

function sendData(e: any) {
    e.preventDefault();
    const name = (<HTMLInputElement>document.querySelector("#name")).value;
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
};

function getDudes(dudes: any) {
    let work = JSON.parse(dudes);
    let dude = document.querySelector("#dude");
    if (dude !== null) {
        dude.innerHTML = ''
            Object.entries(work).forEach((element: any) => {
                let char = element[1];
                if(dude !== null) {
                    dude.innerHTML += char.character_name +'       level: '+  char.character_level+ '<br>'; 
                }
            });
    }
}