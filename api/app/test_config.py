from app.config import get_settings
import os

def test_config_paths():
    settings = get_settings()
    
    # Test if paths exist
    print("\nTesting configuration paths:")
    print("-" * 50)
    
    # Debug prints for path construction
    print(f"Current working directory: {os.getcwd()}")
    print(f"BASE_DIR absolute path: {settings.BASE_DIR.absolute()}")
    print(f"MODEL_PATH absolute path: {settings.MODEL_PATH.absolute()}")
    print(f"INCOME_MODEL_PATH absolute path: {settings.INCOME_MODEL_PATH.absolute()}")
    
    # Test BASE_DIR
    print(f"\nBASE_DIR: {settings.BASE_DIR}")
    print(f"BASE_DIR exists: {settings.BASE_DIR.exists()}")
    
    # Test MODEL_PATH
    print(f"\nLoan Repayment Model Path: {settings.MODEL_PATH}")
    print(f"Model file exists: {settings.MODEL_PATH.exists()}")
    print(f"Model file is file: {settings.MODEL_PATH.is_file()}")
    
    # Test INCOME_MODEL_PATH
    print(f"\nIncome Prediction Model Path: {settings.INCOME_MODEL_PATH}")
    print(f"Income model file exists: {settings.INCOME_MODEL_PATH.exists()}")
    print(f"Income model file is file: {settings.INCOME_MODEL_PATH.is_file()}")
    
    # Print absolute paths for verification
    print("\nAbsolute paths:")
    print(f"Loan Repayment Model: {settings.MODEL_PATH.absolute()}")
    print(f"Income Prediction Model: {settings.INCOME_MODEL_PATH.absolute()}")

if __name__ == "__main__":
    test_config_paths() 