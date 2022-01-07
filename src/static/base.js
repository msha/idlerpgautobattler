document.addEventListener("submit", sendData);

function sendData(e) {
    e.preventDefault();
    const name = document.querySelector("#name").value;

    fetch("/add", {
            method: "POST",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name: parseInt(name),
            })
        })
        .then(res => res.json())
        .then(data => {
            const { result } = data;
            document.querySelector("#dude").innerHTML = data.name;
        })
        .catch(err => console.log(err));
};