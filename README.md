![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-blue.svg) ![Python 3.8.5](https://img.shields.io/badge/Python-3.8.5-brightgreen.svg) ![pandas](https://img.shields.io/badge/Library-pandas-orange.svg) ![scikit-learnn](https://img.shields.io/badge/Library-Scikit_Learn-orange.svg) ![DVC](https://img.shields.io/badge/Library-DVC-orange.svg)  

# ML-Churn Prediction Model Workflow

A Customer Churn Prediction Machine Learning Model Deployed as Web application in Heroku

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
sudo apt-get install python3
sudo apt install python3-pip
sudo apt-get install git
conda create -n env_name python3.8.5 -y
conda activate env_name
pip3 install requirements.txt
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
pip3 install dvc
pip3 install mlflow
```

## Running the tests

- For Automated Testing Write Testing Scripts
- 1. test_config.py
- 2. conftest.py

### Break down into end to end tests

- The Test cases were to check the user input in the following ways
- 1.From Web application Form Response and test Cases were
- 1.1 Checking for form response Correct range
- 1.2 Checking for form response Incorrect range
- 2 From API Response like Postman and Test cases were
- 2.1 Checking for API response Correct range
- 2.2 Checking for API response Incorrect range
- 2.3 Checking for API response Invalid Columns

Run the Automated Test Case by using the Following Commands

```
pytest -v
```

### And Deployment style 

The Deployment Method is Continous Integration / Contionous Deployment / Continous Learning of Model (MLOps)

It is Done by

- github Workflows
- dvc
- mlflow

the following scripts were
```
.github/workflows/ci-cd.yaml
dvc.yaml
```

## Deployment

The Model is Deployed in Heroku in Automatic Deployment Method 

## Built With

* [Python 3.8.5](https://www.python.org/downloads/release/python-385/) - Programming Language
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Web Development Framework
* [DVC](https://dvc.org/) - Used to Track the Data
* [MLFlow](https://mlflow.org/) - Used to Track the Data 
* [MySQL Database](https://dev.mysql.com/doc/) - Data Warehousing
* [Git](https://git-scm.com/doc) - Source Code Management

## Authors

* **Sukil SIva** -  - [Sukil Siva](https://github.com/sukilsiva)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to INeuron AI ML-Flow Community Class
* Inspiration


