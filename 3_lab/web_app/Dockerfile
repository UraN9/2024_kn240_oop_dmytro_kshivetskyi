FROM python:3.12-slim

WORKDIR /app

# Встановлюємо потрібні пакети
RUN pip install --no-cache-dir flask redis psycopg2-binary

# Копіюємо код додатку в контейнер
COPY ./src/web_app /app

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
