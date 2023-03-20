FROM python:3.9-slim

COPY . /aviasales_email_parser

WORKDIR /aviasales_email_parser

RUN pip install -r requirements.txt

CMD ["python", "scheduler.py"]
