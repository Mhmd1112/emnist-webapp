from fastapi import FastAPI, File, UploadFile
import pickle
import numpy as np
from PIL import Image
from tensorflow.keras.models import model_from_json

app = FastAPI()

model_config, model_weights = pickle.load(open("emnist_model.pkl", "rb"))
model = model_from_json(model_config)
model.set_weights(model_weights)
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("L").resize((28, 28))
    data = np.array(image, dtype=np.float32) / 255.0

    data = data.reshape(1, 28 * 28)

    pred = model.predict(data)
    predicted_class = int(np.argmax(pred, axis=1)[0])

    letter = chr(predicted_class + 64)

    return {"prediction": letter}

