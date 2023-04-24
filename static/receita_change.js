// Atribui o elemento do primeiro SelectField
const veiculos = document.getElementById("veiculos");

// Atribui o elemento do segundo SelectField
const receitas = document.getElementById("receitas");

// Adiciona um listener no primeiro SelectField para disparar a mudança no segundo
veiculos.addEventListener("change", function() {
  // Cria um novo evento de mudança
  const event = new Event('change');

  // Define o valor do segundo SelectField com base no valor selecionado no primeiro
  receitas.value = veiculos.value;

  // Dispara o evento de mudança no segundo SelectField
  receitas.dispatchEvent(event);
});
