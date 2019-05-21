#importing libraries
import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request

#creating instance of the flask
app=Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')

#prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,6)
    loaded_model = pickle.load(open("model.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':

     to_predict_array = request.form.to_dict()
     to_predict_array = list(to_predict_array.values())
     to_predict_array = list(map(int, to_predict_array))
     result = ValuePredictor(to_predict_array)
        
     if int(result)==1:
            prediction='S. Robusta'
     elif int(result)==2:
            prediction='F. Ramontchi'
     elif int(result)==3:
            prediction='C. Fistula'
     elif int(result)==4:
            prediction='M. Philippinensis'
     elif int(result)==5:
            prediction='A. Cordifolia'
     elif int(result)==6:
            prediction='C. Infortunatum'
     elif int(result)==7:
            prediction='A. Vasica'
     elif int(result)==8:
            prediction='L. Camara'
     elif int(result)==9:
            prediction='F. Religiosa'
     elif int(result)==10:
            prediction='Murraya'

    return render_template("result.html",prediction=prediction)