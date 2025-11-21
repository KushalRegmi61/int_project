import os
from fastapi import FastAPI
from typing import  List
from contextlib import asynccontextmanager
from pydantic import BaseModel
from transformers import pipeline
from dotenv import load_dotenv


# Load environment variables

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
MODEL_REPO = os.getenv("MODEL_REPO")   # Example: "sentence-transformers/all-MiniLM-L6-v2"

if HF_TOKEN is None:
    raise ValueError("HF_TOKEN is missing in environment variables")

if MODEL_REPO is None:
    raise ValueError("MODEL_REPO is missing in environment variables")



# Request / Response Schemas

class ModelInput(BaseModel):
    text: str





# Global model instance
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the model 
    global predictor
    predictor = pipeline(
        "text-classification",
        model=MODEL_REPO,
        token= HF_TOKEN
        )
    yield
    

app = FastAPI(
    title="Sambodhan Department Classifier API",
    description="AI model that classifies citizen grievances into municipal departments with confidence scores.",
    version="1.0.0",
    lifespan=lifespan
)


# Routes
@app.get("/")
async def root():
    return {"message": "Welcome to the API"}


@app.post("/predict", response_model=List[dict])
async def predict(input_data: ModelInput):
    texts = input_data.text 
    predictions = predictor(texts)
    return predictions



