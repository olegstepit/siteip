# Використовуємо офіційний базовий образ Python
FROM python:3.8-slim

# Встановлюємо залежності
RUN pip install flask requests

# Копіюємо додаток у контейнер
COPY app.py /app.py

# Вказуємо порт, на якому буде працювати додаток
EXPOSE 5000

# Запускаємо додаток
CMD ["python", "/app.py"]
