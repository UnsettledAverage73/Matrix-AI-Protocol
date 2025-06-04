from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Lending Model API"
    
    # Model Settings
    MODEL_PATH: str = "../../Rigorous2/model/loan_repayment_model.pkl"  # Update with your model path
    
    # Security Settings
    API_KEY_HEADER: str = "X-API-Key"
    
    class Config:
        case_sensitive = True
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()