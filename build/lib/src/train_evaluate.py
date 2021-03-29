# load the train and test
# train algo
# save the metrices, params
import os
import warnings
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import precision_recall_fscore_support, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from get_data import read_params
import argparse
import joblib
import json

warnings.filterwarnings("ignore")


def eval_metrics(actual, pred):
    scores_array = np.sqrt(precision_recall_fscore_support(actual, pred))
    Accuracy = accuracy_score(actual, pred)
    
    return scores_array[0], scores_array[1], Accuracy

def train_and_evaluate(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    random_state = config["base"]["random_state"]
    model_dir = config["model_dir"]

    n_estimators_rd = config["estimators"]["RandomForestClassifier"]["params"]["n_estimators"]
    min_samples_split_rd = config["estimators"]["RandomForestClassifier"]["params"]["min_samples_split"]
    min_samples_leaf_rd = config["estimators"]["RandomForestClassifier"]["params"]["min_samples_leaf"]
    max_features_rd = config["estimators"]["RandomForestClassifier"]["params"]["max_features"]
    max_depth_rd = config["estimators"]["RandomForestClassifier"]["params"]["max_depth"]
    criterion_rd = config["estimators"]["RandomForestClassifier"]["params"]["criterion"]

    target = [config["base"]["target_col"]]

    train = pd.read_csv(train_data_path, sep=",")
    test = pd.read_csv(test_data_path, sep=",")

    train_y = train[target]
    test_y = test[target]

    selected_features = ["Contract", "OnlineSecurity", "TechSupport", "tenure", "MonthlyCharges", "SeniorCitizen", "Dependents"]
    
    train_x = train[selected_features]
    test_x = test[selected_features]

    classifier = RandomForestClassifier(
        n_estimators=n_estimators_rd, 
        min_samples_split=min_samples_split_rd,
        min_samples_leaf=min_samples_leaf_rd,
        max_features=max_features_rd,
        max_depth=max_depth_rd,
        criterion=criterion_rd, 
        random_state=random_state)
    classifier.fit(train_x, train_y)

    predicted_qualities = classifier.predict(test_x)
    
    (precision, recall, accuracy) = eval_metrics(test_y, predicted_qualities)

    print("  Precision: %s" % precision[0])
    print("  Recall: %s" % recall[0])
    print("  Model_Score: %s" % accuracy)

#####################################################
    scores_file = config["reports"]["scores"]
    params_file = config["reports"]["params"]

    with open(scores_file, "w") as f:
        scores = {
            "Precision": precision[0],
            "Recall": recall[0],
            "Model_Score": accuracy
        }
        json.dump(scores, f, indent=4)

    with open(params_file, "w") as f:
        params = {
            "n_estimators":n_estimators_rd, 
            "min_samples_split":min_samples_split_rd,
            "min_samples_leaf":min_samples_leaf_rd,
            "max_features":max_features_rd,
            "max_depth":max_depth_rd,
            "criterion":criterion_rd
        }
        json.dump(params, f, indent=4)
#####################################################


    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")

    joblib.dump(classifier, model_path)



if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)