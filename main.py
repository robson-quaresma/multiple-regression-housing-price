from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle
import pandas as pd

# Lambda extraído do modelo
lmbda = 0.21662090066621686

def boxcox_revert(fittedvalue):
    return (fittedvalue * lmbda + 1) ** (1 / lmbda)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame(data, index=[0])

    prediction = model.predict(df)
    result = boxcox_revert(prediction[0]) * 1000
    result = round(result, 2)

    return {'prediction': result}