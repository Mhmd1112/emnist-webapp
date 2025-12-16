import streamlit as st
import requests
from PIL import Image

st.set_page_config(page_title="EMNIST Letter Predictor", layout="centered")

st.title("✍️ EMNIST Letter Prediction")
st.write("Upload a handwritten letter image (28x28 or any size).")

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=200)

    if st.button("🔮 Predict Letter"):
        with st.spinner("Predicting..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/predict",
                    files={"file": uploaded_file}
                )

                if response.status_code == 200:
                    st.success(
                        f"Predicted Letter: **{response.json()['prediction']}**"
                    )
                else:
                    st.error("FastAPI server not responding")

            except Exception as e:
                st.error(f"Error: {e}")
