# Import the necessary libraries
import pickle
from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
import uvicorn



# Load the saved vectorizer
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Load the saved model
with open('my_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Initialize the FastAPI application
app = FastAPI()

# Set up CORS middleware
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define the home page route
@app.get("/home")
def home():
    return "Hello world"

# Define the prediction route
@app.post('/predict')
async def predict(request: Request):
    data = await request.json()
    text = data['text']
    # Vectorize the input text using the trained vectorizer
    input_data = vectorizer.transform([text])
    # Make a prediction using the trained model
    prediction = model.predict(input_data)
    # Convert the prediction to a string label
    polarity = 'Positive' if prediction[0] == 1 else 'Negative'
    proba = model.predict_proba(input_data)[0][1]
    proba = proba if prediction[0] == 1 else 1 - proba

    # Return the prediction results in JSON format
    return {
        'result': polarity,
        'probability': np.float64(proba).item()
    }
    


# Run the application
if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
