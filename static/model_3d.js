const heightInput = document.getElementById("height_cm");
const weightInput = document.getElementById("weight_kg");
const imcDisplay = document.getElementById("imc_val");


const alturaLabel = document.getElementById("altura_val");
const pesoLabel = document.getElementById("peso_val");
      const genderInput = document.getElementById("gender");
      const options = document.querySelectorAll(".gender-option");
      const gripRange = document.getElementById("gripForce");
      const sit_bend_cm = document.getElementById("sit_bend_cm");
      const gripValue = document.getElementById("gripValue");
      const sit_bend_cm_Value = document.getElementById("sit_bend_cm_Value");
      const situps = document.getElementById("situps");
      const situps_Value = document.getElementById("situps_Value");
      const broad_jump_cm = document.getElementById("broad_jump_cm");
      const broad_jump_cm_Value = document.getElementById("broad_jump_cm_Value");

      options.forEach((img) => {
        img.addEventListener("click", () => {
          document.getElementById('init').disabled = false;
          // Desmarcar todas
          options.forEach((i) => i.classList.remove("selected"));
          // Marcar la seleccionada
          img.classList.add("selected");
          console.log ("Selección " + img.dataset.value);
          if (img.dataset.value === "M") {
            gripRange.value = 45;
            gripRange.min = 10;
            gripRange.max = 70;
            //
            sit_bend_cm.value = 20,
            sit_bend_cm.min = 10;
            sit_bend_cm.max = 35;
            //
            situps.value = 45;
            //
            broad_jump_cm.value = 200;
            broad_jump_cm.min = 100;  
            broad_jump_cm.max = 300;
          } else if (img.dataset.value === "F") {
            gripRange.value = 30;
            gripRange.min = 10;
            gripRange.max = 50;
            //
            sit_bend_cm.value = 25,
            sit_bend_cm.min = 20;
            sit_bend_cm.max = 45;
            //
            situps.value = 35;
            //
            broad_jump_cm.value = 150;
            broad_jump_cm.min = 80; 
            broad_jump_cm.max = 250;
          } else {
            gripRange.value = 0;
          }
          gripValue.textContent = gripRange.value;
          // Asignar valor al input hidden
          genderInput.value = img.dataset.value;
        });
      });


      // Mostrar el valor del rango de edad dinámicamente
      const ageInput = document.getElementById("age");
      const ageValue = document.getElementById("age-value");
      ageInput.addEventListener("input", function () {
        ageValue.textContent = ageInput.value;
      });
      gripRange.addEventListener("input", function () {
        gripValue.textContent = gripRange.value;
      });
      sit_bend_cm.addEventListener("input", function () {
        sit_bend_cm_Value.textContent = sit_bend_cm.value;
      });
      situps.addEventListener("input", function () {
        situps_Value.textContent = situps.value;
      });
      broad_jump_cm.addEventListener("input", function () {
        broad_jump_cm_Value.textContent = broad_jump_cm.value;
      });
      // iniciar la tabla
      $(document).ready(function () {
        $("#myTable").DataTable();
      });
function calcularIMC() {
  const altura = parseFloat(heightInput.value);
  const peso = parseFloat(weightInput.value);

  // Mostrar valores o guion si vacío
  alturaLabel.textContent = isNaN(altura) ? "-" : altura;
  pesoLabel.textContent = isNaN(peso) ? "-" : peso;

  if (isNaN(altura) || isNaN(peso) || altura <= 0) {
    imcDisplay.textContent = "-";
    modelo.setAttribute("scale", "1 1 1");
    return;
  }

  const alturaM = altura / 100;
  const imc = peso / (alturaM * alturaM);
  imcDisplay.value = imc;

  // Escalado visual más suave
  let escala;
  if (imc < 18.5) escala = 0.95;
  else if (imc < 25) escala = 1.0;
  else if (imc < 30) escala = 1.08;
  else escala = 1.15;

  // Aplicar escala solo en ancho/profundidad

  // Cambiar color según IMC
}

heightInput.addEventListener("input", calcularIMC);
weightInput.addEventListener("input", calcularIMC);

window.addEventListener("DOMContentLoaded", calcularIMC);


      document
        .getElementById("fitness-form")
        .addEventListener("submit", async function (e) {
          e.preventDefault();

          const formData = new FormData(this);

          // Mostrar los datos ingresados de manera más clara
          const datosIngresados = `
            <ul>
              <li>Edad: ${formData.get("age") || "-"}</li>
              <li>Sexo: ${formData.get("gender") || "-"}</li>
              <li>Altura (cm): ${formData.get("height_cm") || "-"}</li>
              <li>Peso (kg): ${formData.get("weight_kg") || "-"}</li>
              <li>IMC (kg): ${formData.get("body_fat") || "-"}</li>
              <li>diastolica: ${formData.get("diastolic") || "-"}</li>
              <li>systolica: ${formData.get("systolic") || "-"}</li>
              <li>Fuerza de agarre: ${formData.get("gripForce") || "-"}</li>
              <li>Flexión sentado (cm): ${formData.get("sit_bend_cm") || "-"}</li>
              <li>Abdominales: ${formData.get("situps") || "-"}</li>
              <li>Salto largo (cm): ${formData.get("broad_jump_cm") || "-"}</li>
            </ul>
          `;

          try {
            window.test_p.close();
            const response = await fetch(apipref + "/predict", {
              method: "POST",
              body: formData,
            });

            if (!response.ok) {
              throw new Error("Error en la respuesta del servidor" + datosIngresados);
            }

            const result = await response.json();
            const dialog = document.getElementById("predict");
            if (dialog) {
              //
              dialog.showModal();
              //document.getElementById("closeDialogBtn").onclick = () => dialog.close();
            }
            // Puedes personalizar el resultado según la respuesta de la API
            const output = `
              <h3>Resultado del Análisis</h3>
              <h4>Predicción:</h4>
              <pre>${JSON.stringify(result, null, 2)}</pre>
            `;
            
            document.getElementById("result").innerHTML = output;
          } catch (error) {
            document.getElementById("result").innerHTML = `
              <div style="color:red;">Ocurrió un error al procesar la solicitud: ${error.message}</div>
            `;
          }
        });

          function updateValue_sis(value) {
            document.getElementById('rangeValue_sis').innerText = value;
          }
          function updateValue_dia(value) {
            document.getElementById('rangeValue_dia').innerText = value;
          }
