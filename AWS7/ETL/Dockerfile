FROM python:3.10-alpine3.18

WORKDIR /ETL

COPY . .

RUN pip install boto3

CMD ["python","ativ.py"]