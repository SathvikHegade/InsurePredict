# 🏥 InsurePredict

> **AI-powered health insurance premium prediction system with FastAPI & Streamlit**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.31+-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.7.2-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

## 📋 Overview

**InsurePredict** is a production-ready machine learning application that predicts health insurance premium categories (Low, Medium, High) based on user demographics and health metrics. Built with modern Python frameworks, it combines a robust FastAPI backend with an intuitive Streamlit frontend to deliver real-time predictions.

### ✨ Key Features

- 🚀 **Fast REST API** — High-performance `/predict` endpoint built with FastAPI
- 🎨 **Interactive UI** — Clean Streamlit web interface for non-technical users
- 🤖 **ML-Powered** — Random Forest classifier with preprocessing pipeline
- 📊 **Multi-Feature Input** — Considers age, weight, height, income, smoking status, city, and occupation
- ⚡ **Real-time Predictions** — Sub-second response times
- 🔒 **Type-Safe** — Pydantic models for request validation
- 📦 **Production-Ready** — Pinned dependencies, proper error handling, and documentation

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | FastAPI, Uvicorn |
| **Frontend** | Streamlit |
| **ML Framework** | scikit-learn 1.7.2 |
| **Data Processing** | Pandas, NumPy |
| **Model** | Random Forest Classifier |
| **Environment** | Python 3.11+ |

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- pip package manager
- Git (for cloning)

### Installation

1️⃣ **Clone the repository**

```bash
git clone https://github.com/SathvikHegade/InsurePredict.git
cd InsurePredict
```

2️⃣ **Create and activate virtual environment**

**Windows PowerShell:**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux/macOS:**
```bash
python -m venv .venv
source .venv/bin/activate
```

3️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

### 🎯 Usage

#### Option 1: Run Both Services (Recommended)

**Terminal 1 — Start the API server:**
```bash
python -m uvicorn app:app --port 8003
```

**Terminal 2 — Start the Streamlit frontend:**
```bash
streamlit run frontend.py
```

Then open your browser to `http://localhost:8501` and start making predictions!

#### Option 2: API Only

```bash
python -m uvicorn app:app --port 8003 --reload
```

Access interactive API docs at: `http://127.0.0.1:8003/docs`

## 📡 API Documentation

### POST `/predict`

Predicts the insurance premium category for a given profile.

**Request Body:**
```json
{
  "age": 30,
  "weight": 65.0,
  "height": 1.7,
  "income_lpa": 10.0,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

**Response:**
```json
{
  "predicted_category": "Low"
}
```

**Occupation Options:**
`retired`, `freelancer`, `student`, `government_job`, `business_owner`, `unemployed`, `private_job`

## 📂 Project Structure

```
InsurePredict/
├── app.py                 # FastAPI backend with /predict endpoint
├── frontend.py            # Streamlit UI application
├── ml_model.py           # ML model training script
├── model                 # Serialized Random Forest model (pickle)
├── insurance.csv         # Training dataset
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
└── README.md            # Project documentation
```

## 🧠 Model Details

- **Algorithm:** Random Forest Classifier
- **Features:** 7 input features (age, weight, height, income_lpa, smoker, city, occupation)
- **Target:** Premium category (Low / Medium / High)
- **Preprocessing:** ColumnTransformer with OneHotEncoding for categorical features
- **Framework:** scikit-learn 1.7.2 (pinned to avoid version mismatch warnings)

## 🔧 Development

### Running with Hot Reload

```bash
python -m uvicorn app:app --reload --port 8003
```

**Note:** If you encounter reload loops, the file watcher may be picking up changes in `.venv`. Run without `--reload` or exclude the virtual environment directory.

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'sklearn'` | Activate your virtual environment and run `pip install -r requirements.txt` |
| Port already in use | Change the port: `--port 8004` or kill the process using the port |
| Version warnings on model load | Ensure `scikit-learn==1.7.2` is installed (already pinned in requirements.txt) |
| Frontend can't connect to API | Verify API is running on port 8003 and update `API_URL` in `frontend.py` if needed |

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Sathvik Hegade**

- GitHub: [@SathvikHegade](https://github.com/SathvikHegade)
- Repository: [InsurePredict](https://github.com/SathvikHegade/InsurePredict)

---

⭐ **Star this repo if you find it useful!** ⭐