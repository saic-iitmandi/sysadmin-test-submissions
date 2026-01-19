FROM python:3.11-slim

WORKDIR /app

RUN pip install flask gunicorn

COPY app.py .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
