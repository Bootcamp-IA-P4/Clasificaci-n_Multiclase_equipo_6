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
- [Render Deployment](#-render-deployment)
- [Dockerization](#-dockerization).
- [Collaborators](#-collaborators)  
---

##  About the Project

Are you fit enough for a physical challenge, a competitive exam, or an active lifestyle? This project aims to answer that question in less than a second, using just your physical data and a few simple performance tests.

---

## 🔍 Main Features  
✅ Complete EDA process with data cleaning and visualizations.  
✅ Multiclass classification with **Gradient Boosting** model.  
✅ Backend implemented with **Python** and **FastApi**.  
✅ Database integration using **Supabase**.  
✅ Well-organized and modular project structure.  

---

## 🐞 Current Issues  
❌ .

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
  <img src="" alt="Banner centrado" width="900" height="400">
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
  <img src="https://res.cloudinary.com/artevivo/image/upload/v1747826379/Captura_de_pantalla_2025-05-21_091101_r8ouxt.png" alt="Metrics" width="800" height="250">
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

## 🚀 Render Deployment
You can view the live version project at [Render - Clasificación Multiclase](https://clasificaci-n-multiclase-equipo-6.onrender.com).

---

## 🐋 Dockerization

This application is Dockerized. To run it, execute the following command:

```bash
docker-compose up --build
```
---

## 🧑‍💻 Collaborators
This project was developed by the following contributors:
- [Michael López](https://github.com/mikewig/)  
- [Mariela Adimari](https://github.com/marie-adi/)   
- [Nhoeli Salazar](https://github.com/Nho89/)   
- [Juan Carlos Macías](https://github.com/juancmacias/)
---
<p align="right">(<a href="#-index">⬆️ Back to top</a>)</p>
