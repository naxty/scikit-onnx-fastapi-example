FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src /app
WORKDIR /app/

ENV PYTHONPATH=/app

COPY models/boston_housting.onnx /tmp/boston_housing.onnx
ENV MODEL_PATH=/tmp/boston_housing.onnx

EXPOSE 80
EXPOSE 5000