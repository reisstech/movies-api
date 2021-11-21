FROM python:3.8.12-alpine3.13

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt


EXPOSE 5000

ENV FLASK_ENV development

COPY app.py .

CMD [ "flask", "run", "--host", "0.0.0.0" ]
