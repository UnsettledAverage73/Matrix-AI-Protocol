import joblib
import numpy as np
import pandas as pd
from typing import Dict, Any, Tuple
import logging
from .config import get_settings

logger = logging.getLogger(__name__)

class ModelManager:
    def __init__(self):
        settings = get_settings()
        self.repayment_model = None
        self.income_model = None
        self.repayment_model_path = settings.MODEL_PATH
        self.income_model_path = settings.INCOME_MODEL_PATH
        self.load_models()
    
    def load_models(self):
        """Load both models from disk"""
        try:
            self.repayment_model = joblib.load(self.repayment_model_path)
            logger.info(f"Repayment model loaded from {self.repayment_model_path}")
            self.income_model = joblib.load(self.income_model_path)
            logger.info(f"Income model loaded from {self.income_model_path}")
        except Exception as e:
            logger.error(f"Error loading models: {str(e)}")
            raise
    
    def preprocess_income_input(self, features: Dict[str, Any]) -> pd.DataFrame:
        """Preprocess input features for income prediction"""
        # These are the features required by the income model
        income_features = [
            'occupation', 'upi_txns_month', 'mobile_recharge_freq', 'night_light',
            'education', 'is_urban', 'bill_payment_consistency', 'ecommerce_freq',
            'skill_level', 'household_size', 'market_density', 'public_transport_access',
            'housing_type'
        ]
        missing = [f for f in income_features if f not in features]
        if missing:
            raise ValueError(f"Missing required income features: {missing}")
        df = pd.DataFrame([{k: features[k] for k in income_features}])
        return df

    def predict_income(self, features: Dict[str, Any]) -> float:
        """Predict income using the income model"""
        df = self.preprocess_income_input(features)
        prediction = self.income_model.predict(df)[0]
        return float(prediction)

    def preprocess_repayment_input(self, features: Dict[str, Any]) -> np.ndarray:
        """Preprocess input features for repayment prediction"""
        # These are the features required by the repayment model
        required_features = [
            'loan_amount', 'term', 'interest_rate', 'employment_length',
            'annual_income', 'debt_to_income_ratio', 'fico_score',
            'number_of_accounts', 'derogatory_marks', 'revolving_balance',
            'revolving_utilization_rate'
        ]
        missing = [f for f in required_features if f not in features]
        if missing:
            raise ValueError(f"Missing required repayment features: {missing}")
        df = pd.DataFrame([{k: features[k] for k in required_features}])
        return df[required_features].values

    def predict_repayment(self, features: Dict[str, Any]) -> Tuple[float, float, float]:
        """Predict repayment capability using the repayment model"""
        processed_features = self.preprocess_repayment_input(features)
        prediction = self.repayment_model.predict(processed_features)[0]
        probability = self.repayment_model.predict_proba(processed_features)[0][1]
        confidence = abs(probability - 0.5) * 2
        return float(prediction), float(probability), float(confidence)

    def predict_integrated(self, features: Dict[str, Any]) -> Dict[str, Any]:
        """
        Predict income, then use it as 'annual_income' for repayment prediction.
        If 'annual_income' is not provided, use the predicted income.
        """
        # Predict income
        predicted_income = self.predict_income(features)
        # Use predicted income for repayment if not provided
        repayment_features = features.copy()
        if 'annual_income' not in repayment_features or repayment_features['annual_income'] is None:
            repayment_features['annual_income'] = predicted_income
        # Predict repayment
        prediction, probability, confidence = self.predict_repayment(repayment_features)
        return {
            'predicted_income': predicted_income,
            'repayment_prediction': prediction,
            'repayment_probability': probability,
            'repayment_confidence': confidence
        }