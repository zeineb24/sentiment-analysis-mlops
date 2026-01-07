# End-to-End Sentiment Analysis MLOps Pipeline (GCP)

This repository implements a **production-style end-to-end MLOps pipeline** for sentiment analysis using **Google Cloud Platform (GCP)**.  
It covers data preprocessing, model inference, CI/CD, batch prediction, and explainability, following modern MLOps best practices.

---

## 🚀 Project Overview

The goal of this project is to demonstrate how a machine learning model can be:
- trained and containerized,
- deployed as a scalable API,
- integrated into a **batch data processing pipeline**,
- monitored and tested using CI/CD,
- and explained using **XAI techniques**.

This project was built as part of an advanced MLOps workflow and reflects real-world ML system design.

---

## 🏗️ Architecture
BigQuery / GCS
↓
Apache Beam (Dataflow)
↓
Vertex AI / Cloud Run Model Endpoint
↓
Predictions stored in BigQuery
↓
Explainability (SHAP)

## 🧠 Model
- Task: **Sentiment Analysis (binary classification)**
- Algorithms:
  - TF-IDF + Random Forest (scikit-learn)
- Evaluation metrics:
  - Accuracy
  - Precision / Recall
  - F1-score

---

## ⚙️ Tech Stack

- **Python**
- **Google Cloud Platform**
  - BigQuery
  - Cloud Storage (GCS)
  - Vertex AI
  - Cloud Run
  - Cloud Build
  - Dataflow
- **Apache Beam**
- **Docker**
- **scikit-learn**
- **SHAP** (Explainable AI)

---

## 📂 Repository Structure

.
├── beam_clean_pipeline.py # Data cleaning pipeline (Apache Beam)
├── beam_pipeline_to_vertexai.py # Batch prediction pipeline
├── predict.py # Model inference logic
├── xai_ex.py # SHAP explainability
├── Dockerfile # Containerized model
├── cloudbuild.yaml # CI/CD pipeline (Cloud Build)
├── requirements.txt # Python dependencies
├── test_predict.py # Unit tests
├── test_request.py # API request tests
└── README.md

yaml
Copy code

---

## 🔄 MLOps Features Implemented

✔ Data preprocessing with **Apache Beam**  
✔ Batch inference with **Vertex AI / Cloud Run**  
✔ CI/CD automation using **Cloud Build**  
✔ Containerized deployment with **Docker**  
✔ Unit & integration testing  
✔ Model explainability with **SHAP**  

---

## ▶️ How to Run (Locally)

```bash
pip install -r requirements.txt
python predict.py

