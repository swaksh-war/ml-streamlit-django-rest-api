import numpy as np
import pandas as pd
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response

class Prediction(APIView):
    def post(self, request):
        data = request.data
        age = data['age']
        gender = data['gender']
        bp = data['bp']
        cholesterol = data['cholesterol']
        salt = data['salt']
        dtree = DrugConfig.model
        if gender == 'Male':
            gender = 1
        else:
            gender = 0
        
        if bp == 'High':
            bp = 0
        elif bp == 'Low':
            bp = 1
        else:
            bp = 2
        
        if cholesterol == 'High':
            cholesterol = 0
        elif cholesterol == 'Low':
            cholesterol = 1
        else :
            cholesterol = 2
        predictionval = dtree.predict([[age, gender, bp, cholesterol, salt]])
        response_dict = {'p': predictionval}
        print(response_dict)
        return Response(response_dict, status=200)