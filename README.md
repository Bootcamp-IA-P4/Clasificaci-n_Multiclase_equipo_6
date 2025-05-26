<div align="center">
  <img src="https://res.cloudinary.com/artevivo/image/upload/v1747827308/Presentaci%C3%B3n_Ejercicio_y_Entrenamiento_Moderno_Blanco_y_Negro_bevvsf.jpg" alt="Banner centrado" width="900" height="450">
</div>

## 📌 Index
- [About the Project](#-about-the-project)  
- [Main Features](#-main-features)  
- [Current Issues](#-current-issues)
- [Folder Structure](#-folder-structure)
- [Possible Improvements](#-possible-improvements)  
- [Architecture Diagram](#-architecture-diagram)  
- [Installation and Usage](#-installation-and-usage)
- [Model Performance & Hyperparameters](#-model-performance-&-hyperparameters)
- [Testing](#-testing)
- [Demo](#-demo)
- [Render Deployment](#-render-deployment)
- [Dockerization](#-dockerization).
- [System Logs](#-system-logs).
- [Versioned](#-versioned).
- [A/B Testing](#a/b-esting).
- [Collaborators](#-collaborators)  
---

##  About the Project

Are you fit enough for a physical challenge, a competitive exam, or an active lifestyle? This project aims to answer that question in less than a second, using just your physical data and a few simple performance tests.

This multi-class classification project aims to estimate a person's physical performance level (classes A, B, C, or D) based on their body measurements and standardized physical test results.

The model was trained using a dataset from the Korea Sports Promotion Foundation, which includes variables such as age, gender, blood pressure, grip strength, flexibility, and jump distance. These kinds of assessments are commonly used in sports programs, fitness evaluations, or entrance exams for public service roles and can be performed in gyms or training centers.

Although the data originates from Korea, the features used are universal, making the model adaptable to other countries with similar evaluation standards. The goal is to offer a fast, objective tool to support physical readiness without making any personal judgments.

---

## 🔍 Main Features  
✅ Complete EDA process with data cleaning and visualizations.  
✅ Multiclass classification with **Gradient Boosting** model.  
✅ Backend implemented with **Python** and **FastApi**.  
✅ Database integration using **Supabase**.  
✅ Well-organized and modular project structure.  

---

## 🐞 Current Issues  
❌ Enhanced model accuracy necessitates the acquisition of additional data.

---

## 💡 Possible Improvements  
✅ Implement ML Flow.    

---

## 📁 Folder Structure

```bash
# Clasificación_Multiclase_equipo_6
📂 Clasificaci-n_Multiclase_equipo_6
├── 📂 .venv/
├── 📂 .github/
├── 📂 core/
├── 📂 database/  
│   └── supabase_connection.py
├── 📂 static/
│   └── 📂 img
│   └── model_3d.js
│   └── style.css
│── 📂 templates
│   └── index.html              
├── 📂 model/  
│   └── model.pkl
│   └── gender_map.pkl
│   └── class_map.pkl
│   └── testing-model.ipynb
│   └── model.py
│   └── utils.py  
├── 📂 data/
├── 📂 notebook/
│   └── EDA_Clasificacion_multiclase.ipynb
├── 📂 tests/
│   └── test_model.py
├── 📜 .env 
├── 📜 README.md  
├── 📜 .gitignore  
├── 📜 requirements.txt
├── 📜 main.py
├── 📜 dockerfile
├── 📜 compose.yaml
├── 📜 .dockerignore
├── 📜 logs.log
├── 📜 CONTROLVERSION.md
```
---

## 🧠 Architecture Diagram
<div align="center">
  <img src="https://res.cloudinary.com/artevivo/image/upload/v1747994952/Captura_de_pantalla_2025-05-23_120752_apbzb3.png" alt="Banner centrado" width="900" height="400">
</div>
---

## ⚙️ Installation and Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Bootcamp-IA-P4/Clasificaci-n_Multiclase_equipo_6.git
cd Clasificaci-n_Multiclase_equipo_6
```
### 2️⃣ Create and activate the virtual environment
```bash
python -m venv .venv
source .venv/Scripts/activate # Windows
source .venv/bin/activate  # Linux/Mac
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Start the App
```bash
uvicorn main:app --reload
```
---

## 📊 Model Performance & Hyperparameters

<div align="center">
  <img src="https://res.cloudinary.com/artevivo/image/upload/v1748001916/Captura_de_pantalla_2025-05-23_140440_bwr7i4.png" alt="Metrics" width="800" height="350">
</div>
---

## 🧐 Testing
Copy the following command to run the tests:
```bash
python -m unittest tests/test_model.py
```
<div align="center">
  <img src="https://res.cloudinary.com/artevivo/image/upload/v1747826379/Captura_de_pantalla_2025-05-20_111739_stc5vp.png" alt="test" width="500" height="100">
</div>
---

## 📂 Demo
🔗 ▶️ [Ver video - Demo](https://res.cloudinary.com/artevivo/video/upload/v1748255522/0523_djiovy.mov)

---

## 🚀 Render Deployment
You can view the live version project at [Render - Clasificación Multiclase](https://clasificaci-n-multiclase-equipo-6.onrender.com).

---

## 🐋 Dockerization

This application is Dockerized. To run it, execute the following command:

```bash
docker-compose up --build
```
---

## 🚩 System LOgs
The logging system, built with core.lw_log, records every access and prediction made, enabling traceability and auditing of the application's usage.

---

## 📒 Versioned
The system utilizes automatic versioning based on GitHub tags.

Every time the application is deployed, the displayed version corresponds to the latest tag published in the repository, which facilitates change control..

---

## A/B Testing
The project implements an automatic A/B testing system for machine learning models.
Each time new data is generated, a new model (Model B) is trained and its performance is compared to the current production model (Model A) using the macro F1-score on the same validation set.
If Model B outperforms Model A by at least 10% in F1-score, it automatically replaces the production model.
The entire process is logged and recorded in a CSV history for traceability and auditing.

---
## 🧑‍💻 Collaborators
This project was developed by the following contributors:
- [Michael López](https://github.com/mikewig/)  
- [Mariela Adimari](https://github.com/marie-adi/)   
- [Nhoeli Salazar](https://github.com/Nho89/)   
- [Juan Carlos Macías](https://github.com/juancmacias/)
---
<p align="right">(<a href="#-index">⬆️ Back to top</a>)</p>
