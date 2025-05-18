FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /app/

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]

