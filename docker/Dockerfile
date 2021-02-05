FROM tiangolo/meinheld-gunicorn-flask
LABEL maintainer "Raoul Snyman"

COPY . /app
WORKDIR /app/
RUN mv docker/main.py main.py
RUN pip install --no-cache-dir -U pip && pip install --no-cache-dir -r requirements.txt
