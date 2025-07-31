
from fastapi import FastAPI, Request
from pydantic import BaseModel
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import uvicorn

# === Load model and tokenizer ===
model_path = "model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)
model.eval()

# === FastAPI app ===
app = FastAPI()

# === Input format ===
class EmailText(BaseModel):
    text: str

# === Prediction function ===
def classify_email(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.softmax(logits, dim=1)
        prediction = torch.argmax(probs, dim=1).item()
        confidence = probs[0][prediction].item()

        if prediction == 0:
            if confidence < 0.70:
                return f"🤔 Needs Human Opinion (Legit - Confidence: {confidence:.2%})"
            else:
                return f"✅ Legit Email (Confidence: {confidence:.2%})"
        else:
            return f"⚠️ Phishing Email (Confidence: {confidence:.2%})"

# === API route ===
@app.post("/predict")
async def predict(data: EmailText):
    result = classify_email(data.text)
    return {"result": result}
