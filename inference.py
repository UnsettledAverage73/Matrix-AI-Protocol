from fastapi import FastAPI, Request
import pandas as pd
import joblib

model = joblib.load("Rigorous2/model/income_prediction_model.pkl")
app = FastAPI()

@app.post("/invocations")
async def predict(request: Request):
    data = await request.json()
    features = pd.DataFrame([data["features"]])
    prediction = model.predict(features)[0]
    return {"predicted_income": round(prediction, 2)}

@app.get("/ping")
def ping():
    return {"status": "ok"}

