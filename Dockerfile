FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./application /application
WORKDIR /application/

ENV PYTHONPATH=/application

COPY models/boston_housting.onnx /tmp/boston_housing.onnx
ENV MODEL_PATH=/tmp/boston_housing.onnx

EXPOSE 80