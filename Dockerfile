FROM python:3.9.7-slim-bullseye

RUN apt update && apt install -y --no-install-recommends \
    poppler-utils \
    tesseract-ocr

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "-t", "600","server:app"]
