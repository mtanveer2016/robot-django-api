FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Run migrations and start Gunicorn
CMD python manage.py migrate && gunicorn api_project.wsgi:application --bind 0.0.0.0:8000