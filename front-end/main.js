const init = () => {
    document.getElementById('container').innerHTML += '<h3>Ten tekst dodaje wykonanie kodu javascript</h3>';
}

const reqToBackend = () => {
    fetch('http://127.0.0.1:8000/')
}

window.onload = init;