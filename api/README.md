 # Lending Model API

This is a FastAPI-based API for serving lending model predictions.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the api directory with your configuration:
```
MODEL_PATH=path/to/your/model.pkl
```

## Running the API

To run the API in development mode:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Interactive API documentation: `http://localhost:8000/docs`
- Alternative API documentation: `http://localhost:8000/redoc`

## Endpoints

- `GET /`: Welcome message
- `POST /predict`: Make predictions
- `GET /health`: Health check endpoint

## Example Usage

```python
import requests

# Example prediction request
response = requests.post(
    "http://localhost:8000/predict",
    json={
        "features": {
            "feature1": value1,
            "feature2": value2,
            # ... add your features
        }
    }
)

prediction = response.json()
```

## React Native Integration

To use this API in your React Native application:

1. Install axios:
```bash
npm install axios
```

2. Create an API service:
```javascript
import axios from 'axios';

const API_URL = 'http://your-api-url:8000';

export const predict = async (features) => {
  try {
    const response = await axios.post(`${API_URL}/predict`, {
      features: features
    });
    return response.data;
  } catch (error) {
    console.error('Prediction error:', error);
    throw error;
  }
};
```