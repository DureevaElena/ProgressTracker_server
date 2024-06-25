# Используем базовый образ Python
FROM python:3.11

# Устанавливаем переменные среды
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Установка зависимостей
COPY configurations .
RUN pip install --no-cache-dir -r requirements.txt


# Определяем команду для запуска сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
