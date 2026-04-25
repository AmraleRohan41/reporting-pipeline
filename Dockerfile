FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ ./app

WORKDIR /app/app

CMD ["python", "report_gen.py"]