FROM python:3.8-alpine

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt
EXPOSE 8088
CMD ["python", "app.py"]
