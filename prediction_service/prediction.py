import yaml
import json
import os
import numpy as np

class NotinRange(Exception):
    def __init__(self, message = "Values Not in range"):
        self.message = message
        super().__init__(message)

class NotinCols(Exception):
    def __init__(self, message="Values not in Columns"):
        self.message = message
        super().__init__(message)


def get_schema(schema_path="schema_in.json"):
    with open(schema_path) as json_file:
        schema = json.load(json_file)
    return schema

def validate_input(valid_dict=None):
    def _validate_cols(col):
        schema = get_schema()
        actual_cols = schema.keys()
        if col not in actual_cols:
            raise NotinCols
    def _validate_values(col, val):
        schema = get_schema()
        if not (schema[col]["min"] <= float(valid_dict[col]) <= schema[col]["max"]) :
            raise NotinRange

    for col, val in valid_dict.items():
        _validate_cols(col)
        _validate_values(col, val)
    return True