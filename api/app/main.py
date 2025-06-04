from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
from typing import Dict, Any, List
import logging

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

# Input validation model
class PredictionInput(BaseModel):
    features: Dict[str, Any]

# Output validation model
class PredictionOutput(BaseModel):
    prediction: float
    probability: float
    confidence: float

@app.get("/")
async def root():
    return {"message": "Welcome to Lending Model API"}

@app.post("/predict", response_model=PredictionOutput)
async def predict(input_data: PredictionInput):
    try:
        # TODO: Replace this with your actual model prediction
        # This is a placeholder for demonstration
        features = input_data.features
        
        # Mock prediction (replace with your actual model)
        prediction = 0.75  # Example prediction
        probability = 0.85  # Example probability
        confidence = 0.90  # Example confidence
        
        return PredictionOutput(
            prediction=prediction,
            probability=probability,
            confidence=confidence
        )
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}