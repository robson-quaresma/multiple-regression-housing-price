from fastapi import FastAPI
import pickle
import pandas as pd

# Lambda extraído do modelo
lmbda = 0.21662090066621686

def boxcox_revert(fittedvalue):
    return (fittedvalue * lmbda + 1) ** (1 / lmbda)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame(data, index=[0])

    prediction = model.predict(df)
    result = boxcox_revert(prediction[0]) * 1000

    return {'prediction': result}