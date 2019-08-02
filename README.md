# scikit-onnx-fastapi-example

This repository shows how to serve a model with [ONNX Runtime](https://github.com/microsoft/onnxruntime) and fastapi. that was trained with scikit by using ONNX and fastapi. The boston housing dataset from the scikit library was used to train a simple linear regression.

## Training
If you want to take a look on how the model was trained take a look into the notebooks folder. The model is trained with the scikit library and the trained model is exported to ONNX with skl2onnx package.


## Application

![Overview of the application](images/overview.png)
  

## Deployment

Just run ``docker-compose up`` to start the project. The application should be available at http://localhost.