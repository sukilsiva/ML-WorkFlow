
# read the data from data source
# Clean the data
# Do Feature Engineering and Feature selection
# save it in the data/raw for further process
import os
import argparse
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
import joblib
from get_data import read_params, get_data

def load_and_save(config_path):
    config = read_params(config_path)
    scalar_path = config['scalar_path']
    df = get_data(config_path)
    all_features = df.columns
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], downcast='integer', errors='coerce')
    numerical_feature = [feature for feature in df.columns if df[feature].dtypes!="O"]
    numerical_feature.remove('SeniorCitizen')
    for feature in numerical_feature:
        df[feature] = np.log(df[feature])
    categoircal_features = [feature for feature in df.columns if df[feature].dtypes=="O" not in ['customerID']+['Churn']]
    for feature in categoircal_features:
        data = df.copy()
        data["Churn"] = np.where((data["Churn"]=="Yes"),1,0)
        temp = df.groupby(feature)["Churn"].count()/len(data)                       # Collecting the Total Values
        temp_df = temp[temp>0.01].index                                             # Values Greater that .01% index are Noted
        df[feature] = np.where(df[feature].isin(temp_df), df[feature], "Rare_var")  # Replacing rare Variables
    categoircal_features.append("Churn")
    data = df[categoircal_features]                                                                   
    df.drop(categoircal_features, axis=1, inplace=True)                             # Dropping Categorical Vairables
    data = data.apply(LabelEncoder().fit_transform)                                 # Transforming the characters to Labels
    df = pd.concat([df,data], axis=1)
    scaling_feature = [feature for feature in all_features if feature not in ["customerID", "Churn"]]
    df.replace([np.inf, -np.inf], 0, inplace=True)                                  # Replacing inf values with 0
    scaler=MinMaxScaler()
    scaler.fit(df[scaling_feature])
    df = pd.concat([df[["customerID", "Churn"]].reset_index(drop=True),
                    pd.DataFrame(scaler.transform(df[scaling_feature]), columns=scaling_feature)],
                    axis=1)
    df=df[[feature for feature in data.columns]]                                    # Arranging the Columns with respet to dataset
    df.drop("customerID", axis=1, inplace=True)                                     # Dropping CustomerID
    #df.drop(["Churn.1"], axis=1, inplace=True)                # Remove Duplicate Columns
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    df.to_csv(raw_data_path, sep=",", index=False)

    os.makedirs(scalar_path, exist_ok=True)
    scaled_path = os.path.join(scalar_path, "scalar.joblib")

    joblib.dump(scaler, scaled_path)

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config) 