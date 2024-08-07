import joblib
import numpy as np

MLR_from_joblib = joblib.load('my_model_MLR.pkl')

def predict(age,YOE,GF,GM,EB,EM):
    return MLR_from_joblib.predict(np.array([[age,YOE,GF,GM,EB,EM]]))
