FROM python:3.9-slim

COPY . /yandex_afisha

WORKDIR /yandex_afisha

RUN pip install -r requirements.txt

CMD ["python", "scheduler.py"]
