from flask import Flask,request,jsonify
from flask_cors import CORS
import json
import pandas as pd
import predict
import pickle
import numpy as np
# import mongo
lin_model = pickle.load(open('model1.pkl','rb'))
log_model = pickle.load(open('model2.pkl','rb'))
svc_model = pickle.load(open('model3.pkl','rb'))

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return "<p>Hello World</p>"

@app.route('/rec', methods=['POST'])    
def rec():
    jsonData = request.get_json()
    l=[]
    l.append(jsonData['value1'])
    l.append(jsonData['value2'])
    l.append(jsonData['value3'])
    l.append(jsonData['value4'])
    arr = np.array(l, dtype = float)
    print(arr)

    arr2 = arr.reshape(1,-1).astype(np.float32)
    # arr3 = arr2.astype(np.float)
    print(arr2)

    

    ans = predict.classify(log_model.predict(arr2))
    print(log_model.predict(arr2))
    return ans


    


if __name__=='__main__':
    app.run(port = 8000, debug = True)