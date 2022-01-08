document.addEventListener("submit", sendData);

function sendData(e) {
    e.preventDefault();
    const name = document.querySelector("#name").value;
    console.log(name);
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