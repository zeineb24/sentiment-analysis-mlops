import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import csv
import requests
import logging

# GCP config
project_id = "finalproject-456519"
location = "us-central1"

# GCS input and BigQuery output paths
gcs_input_path = "gs://my-bucket-final-project/datasets/datasets_test_data.csv"
bq_output_table = "finalproject-456519.sentiment_dataset.predicted_movie_reviews"
cloud_run_url = "https://sentiment-service-1052343439818.us-central1.run.app/predict"

class PredictSentiment(beam.DoFn):
    def process(self, line):
        try:
            review = next(csv.reader([line]))[0]
            response = requests.post(
                cloud_run_url,
                json={"review": review},
                timeout=10
            )
            prediction = response.json().get("prediction", "error")
            yield {
                "review_text": review,
                "prediction": prediction
            }
        except Exception as e:
            logging.error(f"Prediction failed for line: {line}. Error: {e}")
            yield {
                "review_text": line,
                "prediction": "error"
            }

def run():
    options = PipelineOptions(
        runner="DataflowRunner",
        project=project_id,
        region=location,
        temp_location="gs://my-bucket-final-project/temp",
        staging_location="gs://my-bucket-final-project/staging",
        job_name="predict-sentiment-cloudrun",
        save_main_session=True,
    )

    with beam.Pipeline(options=options) as pipeline:
        (
            pipeline
            | "Read CSV" >> beam.io.ReadFromText(gcs_input_path, skip_header_lines=1)
            | "Predict Sentiment via Cloud Run" >> beam.ParDo(PredictSentiment())
            | "Write to BigQuery" >> beam.io.WriteToBigQuery(
                bq_output_table,
                schema="review_text:STRING, prediction:STRING",
                write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED
            )
        )

if __name__ == "__main__":
    run()
