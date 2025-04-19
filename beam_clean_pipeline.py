import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

class CleanReviewFn(beam.DoFn):
    def process(self, element):
        import csv
        from io import StringIO

        reader = csv.DictReader(StringIO(element))
        for row in reader:
            text = row['review'].strip().lower()
            label = 1 if row['sentiment'].strip().lower() == 'positive' else 0
            yield {'review': text, 'label': label}

def run():
    options = PipelineOptions(
        runner='DataflowRunner',
        project='finalproject-456519',
        temp_location='gs://my-bucket-final-project/temp',
        region='us-central1',
        job_name='imdb-review-cleaning-job'
    )

    with beam.Pipeline(options=options) as pipeline:
        (
            pipeline
            | 'Read CSV Lines' >> beam.io.ReadFromText('gs://my-bucket-final-project/IMDB Dataset.csv', skip_header_lines=1)
            | 'Clean Reviews' >> beam.ParDo(CleanReviewFn())
            | 'Write to BigQuery' >> beam.io.WriteToBigQuery(
                table='finalproject-456519:reviews.cleaned_reviews',
                schema='review:STRING,label:INTEGER',
                write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED
            )
        )

if __name__ == '__main__':
    run()
