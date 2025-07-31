# Netoxa: MiniLM-Based Phishing Detection AI

Netoxa is a production-ready, AI-powered phishing detection system built using a fine-tuned MiniLM model. Trained on real-world Enron and SpamHam datasets, it classifies email content as `phishing` or `legit` with high speed and precision.

---

📚 Datasets Used
This AI phishing detector was trained on a cleaned and balanced dataset of approximately 500,000 emails, sourced from publicly available email corpora:

1.Enron Email Dataset (Data files © Original Authors)

2.Spamhamemails from kaggle (licensed under ODbL)

We carefully cleaned and merged both datasets to ensure high-quality, real-world examples of both legit and phishing/spam emails. This allowed our MiniLM-based model to learn from realistic language patterns found in corporate and malicious communications

---

# Netoxa - AI Phishing Email Detector

🎯 Detect phishing emails using MiniLM AI model.

for demo, please contact.


---

## 🚀 Features
- Real-time email classification
- Lightweight MiniLM model for fast inference
- Gradio-based interactive demo UI
- Confidence score for every prediction
- ONNX model export for multiplatform deployment

---

## 🧠 Model Info
- Architecture: MiniLM (all-MiniLM-L6-v2)
- Format: PyTorch (Hugging Face) + ONNX
- Fine-tuned on: Enron email dataset + SpamHam phishing emails
- Evaluation: Strong legit classification, 70–90% phishing detection based on test samples

---

## 📁 Project Structure

netoxa_project/
├── model/ (Hugging Face format)
├── netoxa.onnx # ONNX model (for multiplatform use)
├── app.py (Gradio demo app)
├── requirements.txt (Training + testing source data)
└── README.md (This file)


---

## 💻 How to Use

### 1. Install Dependencies
```bash
pip install -r requirements.txt

2. Run the Gradio App
python app.py

3. Use the ONNX Model (created to make it multiplatform)
(load the model)
(Run inference with tokenized inputs)

🔐 Licensing & Terms
This project is offered as a premium AI model. Redistribution, resale, or integration into commercial products is strictly prohibited without explicit written permission.

If you wish to integrate Netoxa into your product or platform, please reach out.

💼 Business Inquiries
📧 Contact: prasadmahalle62@gmail.com
💬 Licensing and pricing will be determined after direct communication and negotiation.


⚠️ Legal Notice
All content in this repository — including code, models, and documentation — is protected under applicable copyright and AI licensing laws.
Unauthorized reuse, distribution, or commercial exploitation will result in legal consequences.
