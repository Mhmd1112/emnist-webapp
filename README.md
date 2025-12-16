# EMNIST Letter Prediction WebApp

This is a **handwritten letter recognition web application** using a Neural Network trained on the **EMNIST Letters dataset**.  
The project has a **FastAPI backend** and a **Streamlit frontend** for easy use.

---

## Features

- Predict handwritten letters (A-Z) from images.
- FastAPI server handles the model prediction.
- Streamlit web interface for uploading images and viewing results.
- Model saved as `.pkl` for easy deployment.

---

## Files

- `app.py` → FastAPI backend serving the prediction API.  
- `streamlit_app.py` → Streamlit frontend for user interface.  
- `emnist_model.pkl` → Saved neural network model for predictions.

---

## How to Run Locally

### 1. Install dependencies

```bash
pip install fastapi uvicorn streamlit pillow tensorflow joblib requests
### 2.Running the App
1. Start FastAPI server
python app.py
# or
uvicorn app:app --reload

2. Start Streamlit frontend
streamlit run streamlit_app.py

```bash



