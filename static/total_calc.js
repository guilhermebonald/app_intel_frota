const reg_amount = document.querySelectorAll('#reg-amount');
const reg_value = document.querySelectorAll('#reg-value');
const reg_total = document.querySelectorAll('#reg-total');

const reg_btn = document.querySelector('.reg-form');

window.addEventListener('load', (event) => {
    // event.preventDefault();

    var amount = [];
    var value = [];
    var total = [];

    for (var i = 0; i < reg_amount.length; i++) {
        amount.push(parseFloat(reg_amount[i].textContent));
        value.push(parseFloat(reg_value[i].textContent));
        total = amount[i] * value[i];

        reg_total[i].textContent = "R$ " + parseFloat(total.toFixed(2));
    }

})