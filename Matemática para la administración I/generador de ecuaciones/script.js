// Obtener los elementos HTML relevantes
const gradoSelect = document.querySelector('#grado');
const coeficientesContainer = document.querySelector('#coeficientes-container');
const variablesContainer = document.querySelector('#variables-container');
const resultadoContainer = document.querySelector('#resultado-container');
const formulario = document.querySelector('#formulario');

// Event listener para cambiar el grado de la ecuación
gradoSelect.addEventListener('change', () => {
  // Obtener el grado seleccionado
  const grado = gradoSelect.value;

  // Limpiar los contenedores de coeficientes y variables
  coeficientesContainer.innerHTML = '';
  variablesContainer.innerHTML = '';

  // Generar los campos de coeficientes y variables necesarios
  switch (grado) {
    case '1':
      coeficientesContainer.innerHTML = `
        <label for="coeficiente1">Coeficiente 1:</label>
        <input type="number" id="coeficiente1" name="coeficiente1" required>
      `;
      variablesContainer.innerHTML = `
        <label for="variable">Variable:</label>
        <select id="variable" name="variable">
          <option value="x1">x1</option>
        </select>
      `;
      break;
    case '2':
      coeficientesContainer.innerHTML = `
        <label for="coeficiente1">Coeficiente 1:</label>
        <input type="number" id="coeficiente1" name="coeficiente1" required>
        <label for="coeficiente2">Coeficiente 2:</label>
        <input type="number" id="coeficiente2" name="coeficiente2" required>
      `;
      variablesContainer.innerHTML = `
        <label for="variable1">Variable 1:</label>
        <select id="variable1" name="variable1">
          <option value="x1">x1</option>
        </select>
        <label for="variable2">Variable 2:</label>
        <select id="variable2" name="variable2">
          <option value="x2">x2</option>
        </select>
      `;
      break;
    case '3':
      coeficientesContainer.innerHTML = `
        <label for="coeficiente1">Coeficiente 1:</label>
        <input type="number" id="coeficiente1" name="coeficiente1" required>
        <label for="coeficiente2">Coeficiente 2:</label>
        <input type="number" id="coeficiente2" name="coeficiente2" required>
        <label for="coeficiente3">Coeficiente 3:</label>
        <input type="number" id="coeficiente3" name="coeficiente3" required>
      `;
      variablesContainer.innerHTML = `
        <label for="variable1">Variable 1:</label>
        <select id="variable1" name="variable1">
          <option value="x1">x1</option>
        </select>
        <label for="variable2">Variable 2:</label>
        <select id="variable2" name="variable2">
          <option value="x2">x2</option>
        </select>
        <label for="variable3">Variable 3:</label>
        <select id="variable3" name="variable3">
          <option value="x3">x3</option>
        </select>
      `;
      break;
    default:
      coeficientesContainer.innerHTML = '';
      variablesContainer.innerHTML = '';
  }
});

// Event listener para enviar el formulario
formulario.addEventListener('submit', (event) => {
    event.preventDefault();
  
    // Obtener los valores de los coeficientes y variables
    const grado = gradoSelect.value;
    let coeficiente1, coeficiente2, coeficiente3, variable1, variable2, variable3;
  
    switch (grado) {
      case '1':
        coeficiente1 = Number(document.getElementById('coeficiente1').value);
        variable1 = document.getElementById('variable1').value;
        break;
      case '2':
        coeficiente1 = Number(document.getElementById('coeficiente1').value);
        coeficiente2 = Number(document.getElementById('coeficiente2').value);
        variable1 = document.getElementById('variable1').value;
        variable2 = document.getElementById('variable2').value;
        break;
      case '3':
        coeficiente1 = Number(document.getElementById('coeficiente1').value);
        coeficiente2 = Number(document.getElementById('coeficiente2').value);
        coeficiente3 = Number(document.getElementById('coeficiente3').value);
        variable1 = document.getElementById('variable1').value;
        variable2 = document.getElementById('variable2').value;
        variable3 = document.getElementById('variable3').value;
        break;
    }
  
    // Mostrar la ecuación en el contenedor correspondiente
    let ecuacion;
    switch (grado) {
      case '1':
        ecuacion = `${coeficiente1}${variable1} = 0`;
        break;
      case '2':
        ecuacion = `${coeficiente1}${variable1}^2 + ${coeficiente2}${variable2} = 0`;
        break;
      case '3':
        ecuacion = `${coeficiente1}${variable1}^3 + ${coeficiente2}${variable2}^2 + ${coeficiente3}${variable3} = 0`;
        break;
    }
    ecuacionContainer.innerHTML = `<p>${ecuacion}</p>`;
  });
  
