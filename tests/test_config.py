import json
import logging
import os
import joblib
import pytest
from prediction_service.prediction import validate_input
import prediction_service

input_data = {
    "incorrect_range": 
    {
     "tenure" : 76,
     "MonthlyCharges":5
    },

    "correct_range":
    {
     "tenure" : 66,
     "MonthlyCharges":105
    },

    "incorrect_col":
    {
     "Tenure" : 76,
     "montlycharges":5
    }
}

TARGET_range = {
    "min": 0.0,
    "max": 118.0
}

def test_form_response_correct_range(data=input_data["correct_range"]):
    res = validate_input(data)
    assert  TARGET_range["min"] <= res <= TARGET_range["max"]

#def test_api_response_correct_range(data=input_data["correct_range"]):
#    res = api_response(data)
#    assert  TARGET_range["min"] <= res["response"] <= TARGET_range["max"]

def test_form_response_incorrect_range(data=input_data["incorrect_range"]):
    with pytest.raises(prediction_service.prediction.NotinRange):
        res = validate_input(data)

#def test_api_response_incorrect_range(data=input_data["incorrect_range"]):
#    res = api_response(data)
#    assert res["response"] == prediction_service.prediction.NotinRange().message

def test_api_response_incorrect_col(data=input_data["incorrect_col"]):
    res = validate_input(data)
    assert res["response"] == prediction_service.prediction.NotinCols