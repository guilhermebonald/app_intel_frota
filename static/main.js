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
        .then(data => {
            const lastCarIndex = data.length - 1;
            const lastCar = data[lastCarIndex];

            const tbody = document.querySelector('.my-table-body-cars');
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${lastCar.frota}</td>
                <td>${lastCar.placa}</td>
                <td>
                    <form action="/update_car/${data.id}">
                        <input type="hidden" name="csrf_token" value="{{ form.csrf_token._value() }}">
                        <button class="btn btn-info btn-sm edit-btn">Editar</button>
                    </form>
                </td>
                <td>
                    <form action="/delete_car/${data.id}">
                        <input type="hidden" name="csrf_token" value="{{ form.csrf_token._value() }}">
                        <button class="btn btn-danger btn-sm delete-btn">Deletar</button>
                    </form>
                </td>
            `;
            tbody.appendChild(row)
        })
        .catch(error => console.error(error))
})