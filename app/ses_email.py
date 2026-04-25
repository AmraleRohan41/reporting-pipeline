import boto3
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from config import AWS_REGION, EMAIL_FROM, EMAIL_TO


def send_email_ses(file_name):
    client = boto3.client("ses", region_name=AWS_REGION)

    msg = MIMEMultipart()
    msg["Subject"] = "Automated Report via AWS SES"
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO

    with open(file_name, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())

    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={file_name}")
    msg.attach(part)

    response = client.send_raw_email(
        Source=EMAIL_FROM,
        Destinations=[EMAIL_TO],
        RawMessage={"Data": msg.as_string()}
    )

    print("SES Email sent:", response["MessageId"])