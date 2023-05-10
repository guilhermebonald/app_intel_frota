fetch('/veiculos')
    .then(response => response.json())
    .then(items => {
        const table = document.querySelector('#myTable tbody');
        table.innerHTML = '';

        items.forEach(i => {
            const tr = document.createElement('tr')
            tr.innerHTML = `
                <td>${ i.frota }</td>
                <td>${ i.placa }</td>
                <td>
                    <form action="/update_car/${i.id}">
                        <input type="hidden" name="csrf_token" value="{{ form.csrf_token._value() }}">
                        <button type="submit" class="btn btn-info btn-sm edit-btn">Editar</button>
                    </form>
                </td>
                <td>
                    <form action="/delete_car/${i.id}">
                        <input type="hidden" name="csrf_token" value="{{ form.csrf_token._value() }}">
                        <button type="submit" class="btn btn-danger btn-sm delete-btn">Excluir</button>
                    </form>
                </td>
            `;
            table.appendChild(tr);
        });
    });