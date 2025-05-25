const heightInput = document.getElementById("height_cm");
const weightInput = document.getElementById("weight_kg");
const imcDisplay = document.getElementById("imc_val");
const alturaLabel = document.getElementById("altura_val");
const pesoLabel = document.getElementById("peso_val");
const genderInput = document.getElementById("gender");
const options = document.querySelectorAll(".gender-option");
const gripRange = document.getElementById("gripforce");
const sit_bend_cm = document.getElementById("sit_bend_cm");
const gripValue = document.getElementById("gripValue");
const situps = document.getElementById("situps");
const broad_jump_cm = document.getElementById("broad_jump_cm");
const diastolic = document.getElementById("diastolic");
const systolic = document.getElementById("systolic");

updateValue_sis(systolic.value);
updateValue_dia(diastolic.value);
updateValue_sit_bend_cm(sit_bend_cm.value);
updateValue_situps(situps.value);
updateValue_broad_jump_cm(broad_jump_cm.value);

options.forEach((img) => {
  img.addEventListener("click", () => {
    document.getElementById("init").disabled = false;
    // Desmarcar todas
    options.forEach((i) => i.classList.remove("selected"));
    // Marcar la seleccionada
    img.classList.add("selected");
    console.log("Selección " + img.dataset.value);
    if (img.dataset.value === "M") {
      gripRange.value = 45;
      //
      sit_bend_cm.value = 20;
      //
      situps.value = 45;
      //
      broad_jump_cm.value = 180;
    } else if (img.dataset.value === "F") {
      gripRange.value = 30;
      //
      sit_bend_cm.value = 25;
      //
      situps.value = 35;
      //
      broad_jump_cm.value = 150;
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
              <li>Fuerza de agarre: ${formData.get("gripforce") || "-"}</li>
              <li>Flexión sentado (cm): ${
                formData.get("sit_bend_cm") || "-"
              }</li>
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

      console.log("Prediction:", result[0] + " " + result[1]);

      let output = `
        <h4>Predicción:</h4>
        <pre>${result[0].prediction}</pre>
      `;

      document.getElementById("result").innerHTML = output;
      radarChart.data.labels = [
        //"Edad",
        //"Altura (cm)",
        //"Peso (kg)",
        //"IMC (%)",
        //"Diastólica",
        //"Sistólica",
        "F. agarre",
        "Flexión sentado",
        "Abdominales",
        "Salto largo",
      ];
      radarChart.data.datasets[0].data = [
        //result[1].age,
        //result[1].height_cm,
        //result[1].weight_kg,
        //result[1].body_fat_percent,
        //result[1].diastolic,
        //result[1].systolic,
        result[1].gripforce,
        result[1].sit_and_bend_forward_cm,
        result[1].sit_ups_counts,
        result[1].broad_jump_cm * 0.3,
      ];

      // Añadir otra fuente de datos como un nuevo dataset
      if (result.length > 2 && result[2]) {
        // Si ya existe un segundo dataset, actualízalo; si no, agrégalo
        if (radarChart.data.datasets.length > 1) {
          radarChart.data.datasets[1].data = [
            //result[2].diastolic,
            //result[2].systolic,
            result[2][0],
            result[2][1],
            result[2][2],
            result[2][3] * 0.3,
          ];
        } else {
          radarChart.data.datasets.push({
            label: "Comparación",
            data: [
              //result[2].diastolic,
              //result[2].systolic,
              result[2][0],
              result[2][1],
              result[2][2],
              result[2][3] * 0.3,
            ],
            backgroundColor: "rgba(255,99,132,0.2)",
            borderColor: "rgba(255,99,132,1)",
            borderWidth: 1,
          });
        }
      }
      radarChart.update();
    } catch (error) {
      document.getElementById("result").innerHTML = `
              <div style="color:red;">Ocurrió un error al procesar la solicitud: ${error.message}</div>
            `;
    }
  });

function updateValue_sis(value) {
  document.getElementById("rangeValue_sis").innerText = value;
}
function updateValue_dia(value) {
  document.getElementById("rangeValue_dia").innerText = value;
}
function updateValue_sit_bend_cm(value) {
  document.getElementById("sit_bend_cm_Value").innerText = value;
}
function updateValue_situps(value) {
  document.getElementById("situps_Value").innerText = value;
}
function updateValue_broad_jump_cm(value) {
  document.getElementById("broad_jump_cm_Value").innerText = value;
}
