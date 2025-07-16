FROM python:3.12.11-alpine3.22

ARG SRC_DIR

COPY requirements.txt .

COPY .env .

RUN pip install -r requirements.txt

COPY ${SRC_DIR}/ .

CMD ["python", "main.py"]