const form = document.querySelector('#car-form');

form.addEventListener('submit', (event) => {
    // evita que o navegador execute a função pelo link, e execute somente pela função Fetch
    event.preventDefault();

    const formData = new FormData(form);
    formData.append('csrf_token', '{{ form.csrf_token._value() }}');

    const options = {
        method: 'POST',
        body: formData
    }

    fetch('/add_car', options)
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error))
})