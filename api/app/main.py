from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
from typing import Dict, Any, List
import logging
from .model_utils import ModelManager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Lending Model API",
    description="API for serving lending model predictions",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize model manager
model_manager = ModelManager()

# Input validation model
class PredictionInput(BaseModel):
    features: Dict[str, Any]

# Output validation model for repayment
class PredictionOutput(BaseModel):
    prediction: float
    probability: float
    confidence: float

# Output validation model for integrated prediction
class IntegratedPredictionOutput(BaseModel):
    predicted_income: float
    repayment_prediction: float
    repayment_probability: float
    repayment_confidence: float

@app.get("/")
async def root():
    return {"message": "Welcome to Lending Model API"}

@app.post("/predict", response_model=PredictionOutput)
async def predict(input_data: PredictionInput):
    try:
        prediction, probability, confidence = model_manager.predict_repayment(input_data.features)
        return PredictionOutput(
            prediction=float(prediction),
            probability=float(probability),
            confidence=float(confidence)
        )
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict/income")
async def predict_income(input_data: PredictionInput):
    try:
        predicted_income = model_manager.predict_income(input_data.features)
        return {"predicted_income": predicted_income}
    except Exception as e:
        logger.error(f"Income prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict/integrated", response_model=IntegratedPredictionOutput)
async def predict_integrated(input_data: PredictionInput):
    try:
        result = model_manager.predict_integrated(input_data.features)
        return IntegratedPredictionOutput(**result)
    except Exception as e:
        logger.error(f"Integrated prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}