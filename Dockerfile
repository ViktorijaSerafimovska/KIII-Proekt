FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install psycopg2-binary flask-migrate

COPY . .

ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

RUN flask db init || true  

EXPOSE 5000

CMD ["sh", "-c", "flask db upgrade && flask run"]