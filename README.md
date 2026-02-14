# FastAPI Health Insurance Premium Predictor

Minimal project that exposes a `/predict` endpoint (FastAPI) and a Streamlit frontend (`frontend.py`).

Quick start

1. Create and activate a virtual environment (Windows PowerShell):

```powershell
python -m venv .venv-1
& .venv-1\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Start the API server (uses `app:app`). Recommended port: `8003`:

```powershell
python -m uvicorn app:app --port 8003
```

4. Start the Streamlit frontend (default expects API on `http://127.0.0.1:8003`):

```powershell
streamlit run frontend.py
```

Notes
- The model was saved with `scikit-learn==1.7.2`; `requirements.txt` pins that version to avoid unpickle warnings.
- If you want hot-reload for the API, run `uvicorn` with `--reload` but exclude the venv from watch to prevent reload loops.