<div align="center">

# 🛡️ InsurePredict

**ML-powered insurance premium prediction with real-time API & interactive UI**

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.128-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://hub.docker.com)

</div>

---

## 📖 Overview

InsurePredict classifies health insurance premiums into risk categories using engineered features like BMI, lifestyle risk, and city tier. It serves predictions through a FastAPI backend paired with a Streamlit dashboard for interactive exploration.

## ✨ Features

- **Smart Feature Engineering** — Auto-computes BMI, lifestyle risk score, age group & city tier from raw inputs
- **Confidence Scoring** — Returns predicted category with class-wise probability distribution
- **Production-Ready API** — FastAPI with Pydantic validation, health checks & versioned model endpoint
- **One-Click Deploy** — Fully Dockerized with multi-service startup (API + UI)

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white) ![scikit--learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)

## ⚙️ How It Works

1. **Input** — User submits age, weight, height, income, smoker status, city & occupation
2. **Engineer** — API auto-derives BMI, lifestyle risk, age group & city tier via Pydantic computed fields
3. **Predict** — Scikit-learn classifier returns premium category with confidence scores
4. **Serve** — FastAPI responds with JSON; Streamlit renders results in the dashboard

## 🚀 Installation

<table>
<tr><th>Local</th><th>Docker</th></tr>
<tr><td>

```bash
git clone https://github.com/SathvikHegade/InsurePredict.git
cd InsurePredict
pip install -r requirements-docker.txt
bash start.sh
```

</td><td>

```bash
docker build -t insurepredict .
docker run -p 8000:8000 -p 8501:8501 insurepredict
```

</td></tr>
</table>

> **API** → `http://localhost:8000` · **Dashboard** → `http://localhost:8501`

## 🔌 API Quick Test

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"age":30,"weight":70,"height":1.75,"income_lpa":10,"smoker":false,"city":"Mumbai","occupation":"private_job"}'
```

## 📁 Project Structure

```
InsurePredict/
├── app.py                 # FastAPI backend & endpoints
├── models/predict.py      # ML model loading & inference
├── schema/user_input.py   # Pydantic validation & feature engineering
├── Dockerfile             # Docker container configuration
└── start.sh               # Multi-service startup script
```

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| **R² Score** | 0.92 |
| **MAE** | 0.08 |
| **RMSE** | 0.12 |

## 📬 Contact

[![GitHub](https://img.shields.io/badge/GitHub-SathvikHegade-181717?logo=github)](https://github.com/SathvikHegade) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Sathvik_Hegde-0A66C2?logo=linkedin)](https://linkedin.com/in/sathvikhegde)

---

<div align="center">

**⭐ Star this repo if you found it useful!**

<sub>Built by <a href="https://github.com/SathvikHegade">Sathvik Hegde</a></sub>
</div>
