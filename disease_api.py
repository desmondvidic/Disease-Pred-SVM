from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load trained model and vectorizer
text_clf = joblib.load("disease_prediction_model.pkl")  # Save your trained model separately
ds = pd.read_csv("symptom_Description.csv", index_col="Disease")
pr = pd.read_csv("symptom_precaution.csv", index_col="Disease")

# Fill NaN values in precautions dataset
pr = pr.fillna("")
pr["precautions"] = pr.apply(lambda row: ", ".join(row.dropna()), axis=1)

# Initialize FastAPI app
app = FastAPI()


# Define input data model
class SymptomsInput(BaseModel):
    symptoms: str  # User enters symptoms as a single string


@app.get("/")
def home():
    return {"message": "Disease Prediction API is Live!"}


@app.post("/predict")
def predict_disease(data: SymptomsInput):
    # Transform symptoms using trained TF-IDF vectorizer
    symptoms_tfidf = text_clf.named_steps['tfidf'].transform([data.symptoms])

    # Predict disease
    predicted_disease = text_clf.named_steps['clf'].predict(symptoms_tfidf)[0]

    # Get disease description
    disease_description = ds.loc[
        predicted_disease, "Description"] if predicted_disease in ds.index else "No description available"

    # Get precautions
    disease_precautions = pr.loc[
        predicted_disease, "precautions"] if predicted_disease in pr.index else "No precautions available"

    return {
        "Predicted Disease": predicted_disease,
        "Description": disease_description,
        "Precautions": disease_precautions
    }

