# 📊 Reporting Pipeline (Docker + AWS SES + S3)

This project is a **Python-based automated reporting pipeline** that:
- Generates a report
- Uploads it to AWS S3
- Sends an email notification using AWS SES

The entire workflow is containerized using Docker for easy deployment and portability.

---

## 🚀 Features

- 📁 Report generation using Python
- ☁️ Upload reports to AWS S3
- 📧 Send email notifications via AWS SES
- 🐳 Fully containerized using Docker
- 🔐 Environment variable-based configuration

---

## ⚙️ Prerequisites

Make sure you have:

- Docker installed
- AWS account
- Configured:
  - S3 bucket
  - SES (email verified)

---

## 🔐 Environment Variables

Create a `.env` file:

AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=ap-south-1

S3_BUCKET_NAME=your_bucket_name

SENDER_EMAIL=your_verified_email
RECEIVER_EMAIL=receiver_email

---

🐳 Docker Setup

1. Build Docker Image
docker build -t report-pipeline .

2. Run Container
docker run --env-file .env report-pipeline

---

📤 Workflow

1. Python script generates report
2. Report uploaded to S3 bucket
3. Email notification sent via SES

---

📬 Sample Output

Uploaded to S3
SES Email sent: <message-id>

---

⚠️ Important Notes

* If using AWS SES in sandbox mode, verify both sender and receiver emails.
* Emails may go to Spam initially — configure SPF/DKIM/DMARC for better delivery.
* Ensure IAM user has permissions:
    * AmazonS3FullAccess
    * AmazonSESFullAccess


