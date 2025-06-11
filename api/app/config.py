from pydantic_settings import BaseSettings
from functools import lru_cache
from pathlib import Path

class Settings(BaseSettings):
    # Base Directory Settings
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
    
    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Lending Model API"
    
    # Model Settings
    MODEL_PATH: Path = (BASE_DIR / "Rigorous2" / "model" / "loan_repayment_model.pkl").resolve()
    INCOME_MODEL_PATH: Path = (BASE_DIR / "Rigorous2" / "model" / "income_prediction_model.pkl").resolve()
    
    # Security Settings
    API_KEY_HEADER: str = "X-API-Key"
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("Settings __init__: __file__ is", __file__)
        # Verify that model files exist
        if not self.MODEL_PATH.exists():
            raise FileNotFoundError(f"Loan repayment model not found at: {self.MODEL_PATH}")
        if not self.INCOME_MODEL_PATH.exists():
            raise FileNotFoundError(f"Income prediction model not found at: {self.INCOME_MODEL_PATH}")
    
    class Config:
        case_sensitive = True
        env_file = ".env"

# @lru_cache()
def get_settings():
    return Settings()
