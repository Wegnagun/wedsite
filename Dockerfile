FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt
COPY . .
CMD ["gunicorn", "weddingsite.wsgi:application", "--bind", "0:8000" ]