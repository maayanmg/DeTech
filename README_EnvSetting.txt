README:
How to set python environment to have a running web server that accepts query for pneumonia detection

Create virtual python environment
> virtualenv env

Create and activate virtual python environment (on macOS)
> python3 -m venv myenv
> source venv/bin/activate

Activate the virtual environment
> env\Scripts\activate

Install required packages
> pip install -r requirements_venv.txt --trusted-host files.pythonhosted.org

Run the web server
> uvicorn --host 0.0.0.0 --port 5000 classifier.app:app

Open web browser
http://localhost:5000/docs

Run request from command line
> curl -X POST "http://localhost:5000/pneumonia/predict" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "image_file=@D:\Projects\pneumonia-detection\fixtures\test_normal_1.jpeg;type=image/jpeg"

Freeze the env and save requirements
> pip freeze > requirements_venv.txt

Run Qt Designer
> (env) D:\Projects\pneumonia-detection\env>Lib\site-packages\qt5_applications\Qt\bin\designer.exe

Web resources/guide and tutorials
https://realpython.com/qt-designer-python/#installing-and-running-qt-designer

Convert PyQT ui to python source code
> (env) D:\Projects\pneumonia-detection> pyuic5.exe -x app_code\progress_bar.ui -o progress_bar.py

Deep Learning for Detecting Pneumonia from X-ray Images
> https://www.kaggle.com/code/amyjang/tensorflow-pneumonia-classification-on-x-rays
> https://towardsdatascience.com/deep-learning-for-detecting-pneumonia-from-x-ray-images-fc9a3d9fdba8

This the project we are baseed on
> https://towardsdatascience.com/pneumonia-detection-with-keras-and-fastapi-6c10dab657e0

fastai book
> https://github.com/fastai/fastbook/blob/master/13_convolutions.ipynb

dataset Chest X-Ray Images (Pneumonia)
> https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia

keras 
> https://www.tutorialspoint.com/keras/index.htm
> https://keras.io/api/models/model/

GitHub that uses FastAPI and router lets access the module (the one we cloned)
> https://github.com/happilyeverafter95/pneumonia-detection

FastAPI Guide
> https://reshetech.co.il/python-tutorials/fastapi-probably-the-best-python-web-framework

FastAPI: The simplest FastAPI file could look like this
> https://fastapi.tiangolo.com/tutorial/first-steps/

TensorFlow
> https://www.tensorflow.org/api_docs/python/tf/Graph
> https://www.tensorflow.org/guide/intro_to_graphs?hl=he
> https://analyticsindiamag.com/a-complete-understanding-of-dense-layers-in-neural-networks/