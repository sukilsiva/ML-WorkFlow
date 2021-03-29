import pandas as pd
import sqlalchemy
import argparse
import yaml

pd.pandas.set_option("display.max_columns", None)

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_input_data(config_path):
    config = read_params(config_path)
    #print(config)
    data_path=config["data_source"]["sql_source"]
    db = yaml.full_load(open('database.yaml'))
    username = db['mysql_user']
    password = db['mysql_password']
    host = db['mysql_host']
    dbname = db['mysql_db']
    #print(username, password, host, dbname)
    #print("mysql+pymysql://"+username+":"+password+"@"+host+"/"+dbname)
    engine = sqlalchemy.create_engine("mysql+pymysql://"+username+":"+password+"@"+host+"/"+dbname)
    original_data = pd.read_sql_table("customerdata",engine)
    app_data = pd.read_sql_table("webappdata",engine)
    data = pd.concat([original_data, app_data], axis=0)
    data = data.iloc[:, :-1]
    #print(data.head())
    data.to_csv(data_path,sep=",",encoding="utf-8", index=False)
    return data

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    results=get_input_data(config_path=parsed_args.config)
    