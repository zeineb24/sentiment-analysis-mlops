FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code and model files
COPY predict.py model.joblib vectorizer.joblib ./

# Expose port and run app
CMD ["python", "predict.py"]
