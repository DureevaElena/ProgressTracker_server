
FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY configurations .
RUN pip install --no-cache-dir -r requirements.txt

#CMD ["python", "manage.py", "runserver", "127.0.0.1:800"]
CMD ["gunicorn", "configurations.wsgi:application", "--bind", "0.0.0.0:8002"]