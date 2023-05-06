const form = document.querySelector('#car-form');

form.addEventListener('submit', (event) => {
    // evita que o navegador execute a função pelo link, e execute somente pela função Fetch
    event.preventDefault();

    const formData = new FormData(form);

    fetch('/add_car',
        {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => { console.log(data) })
        .catch(error => console.error(error))
})