from fastapi import FastAPI
import pickle
import pandas as pd


with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame(data, index=[0])

    prediction = model.predict(df)

    return {'prediction': prediction[0]}