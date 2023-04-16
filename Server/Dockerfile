FROM python:3.8-alpine

WORKDIR /app
COPY requirements.txt requirements.txt
COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
