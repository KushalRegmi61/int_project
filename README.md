# Sambodhan  Urgency Classifier

Sambodhan  Urgency Classifier: An AI-powered system to classify citizen grievances into municipal urgency levels.

## Setup

1. Clone the repository
2. Create a `.env` file in the root directory with the following variables:
    ```
    HF_TOKEN=your_huggingface_token_here
    MODEL_REPO=your_model_repo_id_here
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Project

This project consists of two components that need to run simultaneously:

### 1. Start the Backend API (FastAPI)
```bash
cd backend
uvicorn backend.main:app --reload
```
The API will run on `http://127.0.0.1:8000`

### 2. Start the Frontend (Streamlit)
In a new terminal:
```bash
streamlit run app.py
```
The Streamlit app will open in your browser at `http://localhost:8501`

## Environment Variables

- `HF_TOKEN`: Your Hugging Face API token (required for model access)
- `MODEL_REPO`: The Hugging Face model repository ID (e.g., "username/model-name")

## Usage

1. Ensure both backend and frontend are running
2. Open the Streamlit app in your browser
3. Enter a citizen grievance in the text area
4. Click "Classify" to get the urgency prediction with confidence score