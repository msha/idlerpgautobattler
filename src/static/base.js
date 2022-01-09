document.addEventListener("submit", sendData);
document.addEventListener("update", getDudes);

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
        .then(res => res.json())
        .then(data => {
            const { result } = data;
            document.querySelector("#dude").innerHTML = data.return;
        })
        .catch(err => console.log(err));
};

function getDudes(e) {
    fetch("/get_dudes", {
            method: "GET",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json"
            }
        })
        .then(res => res.json())
        .then(data => {
            document.querySelector("#dude").innerHTML = ''
            data.forEach(element => {
                document.querySelector("#dude").innerHTML += element.character_name + '<br>';
            });

        })

}

setInterval(function() {
    getDudes();
}, 500);