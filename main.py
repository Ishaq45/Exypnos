import uvicorn
from fastapi import FastAPI
from InputModel import InputModel
import numpy as np
import pickle
import pandas as pd


app = FastAPI()
pickle_in = open("model_built_fapi.pkl", "rb")
regressor = pickle.load(pickle_in)


@app.get('/')
def index():
    return {'message': 'Hello, world'}

@app.get('/Welcome')
def get_name(name : str):
    return {'Welcome to my local webpage ': f'{name}'}



@app.post('/predict')
def predict_yValue(data : InputModel):
    data = data.dict()
    print(data)
    x = data['xValue']
    print(x)
    prediction = regressor.predict([[x]])
    return {
        'prediction' : 'The value of y is : {}'.format(prediction[0])
        }



if __name__=="__main__":
 uvicorn.run(app)