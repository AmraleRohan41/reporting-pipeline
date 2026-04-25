import pandas as pd
import boto3

from config import AWS_BUCKET, AWS_REGION
from ses_email import send_email_ses


def generate_report():
    df = pd.DataFrame({
        "TicketID": [1, 2, 3],
        "Status": ["Open", "Closed", "Pending"],
        "Client": ["A", "B", "C"]
    })

    file_name = "report.xlsx"
    df.to_excel(file_name, index=False)
    return file_name


def upload_to_s3(file_name):
    s3 = boto3.client("s3", region_name=AWS_REGION)
    s3.upload_file(file_name, AWS_BUCKET, file_name)
    print("Uploaded to S3")


if __name__ == "__main__":
    file = generate_report()
    upload_to_s3(file)
    send_email_ses(file)