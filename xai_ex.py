# xai_explain.py

import shap
import joblib
import matplotlib.pyplot as plt
from google.cloud import storage
import numpy as np


def upload_to_gcs(bucket_name, source_file, dest_blob):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(dest_blob)
    blob.upload_from_filename(source_file)
    print(f"✅ Uploaded to GCS: {dest_blob}")


# Load model and vectorizer
model = joblib.load("model.joblib")
vectorizer = joblib.load("vectorizer.joblib")

# Sample reviews
sample_reviews = [
    "I loved the movie, it was fantastic!",
    "This film was awful. I wouldn't recommend it.",
    "Absolutely brilliant and well-acted.",
    "Not my type of movie, quite boring.",
]

# Vectorize and convert to dense for SHAP
X_transformed = vectorizer.transform(sample_reviews).toarray()

# SHAP KernelExplainer (works better for text + sklearn models)
explainer = shap.KernelExplainer(model.predict_proba, shap.kmeans(X_transformed, 2))
shap_values = explainer.shap_values(X_transformed)

# Plot summary for class 1 (positive sentiment)
shap.summary_plot(shap_values[1], features=X_transformed, feature_names=vectorizer.get_feature_names_out(), show=False)
plt.savefig("shap_summary.png")
print("✅ SHAP explainability plots saved.")

# Upload to GCS
upload_to_gcs("my-bucket-final-project", "shap_summary.png", "explainability/shap_summary.png")
