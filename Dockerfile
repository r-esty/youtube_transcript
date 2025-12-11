FROM python:3.11-slim-bookworm

WORKDIR /app

ADD . /app

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "transcript_scrape.py"]