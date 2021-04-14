const bindButton = () => {
    console.log(document.getElementById("submit"))
    document.getElementById("submit").addEventListener("click", () => {
        let login = document.getElementById("login").value
        fetch(`http://127.0.0.1:8000/getUserRole?login=${login}`)
            .then(res => res.json())
            .then(res => {
                console.log(res);
        })
    });
}


const testReqToBackend = () => {
    fetch('http://127.0.0.1:8000/')
        .then(res => res.json())
        .then(res => {
            console.log(res);
    })
}

window.onload = () => {
    bindButton();
    document.getElementById('container').insertAdjacentHTML('beforeend','<h3>Ten tekst dodaje wykonanie kodu javascript</h3>');
}