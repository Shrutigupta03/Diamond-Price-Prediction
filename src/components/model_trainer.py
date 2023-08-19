import numpy as np 
import pandas as pd
import os, sys 
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from src.exception import CustomException
from src.logger import logging

from src.utils import save_object
from src.utils import evaluate_model
from dataclasses import dataclass


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_training(self, train_array, test_array):
        try:
            logging.info('Splitting Dependent & Independent variables from train & test data')
            X_train, y_train, X_test, y_test =(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models={
            'LinearRegression':LinearRegression(),
            'Lasso':Lasso(),
            'Ridge': Ridge(),
            'ElasticNet': ElasticNet(),
            'DecisionTree':DecisionTreeRegressor(),
            'RandonForest':RandomForestRegressor()
        }

            model_report:dict=evaluate_model(X_train, y_train, X_test, y_test, models)
            print('\n=====================================================================')
            logging.info(f'Model Evaluation Report : {model_report}')

            # To get best model score from dictionary
            best_model_score = max(sorted(model_report.values()))
            
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            print(f'Best Model Found, Model Name : {best_model_name}, Model Score : {best_model_score}')
            print('\n=====================================================================')
            logging.info(f'Best Model Found, Model Name : {best_model_name}, Model Score : {best_model_score}')

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )


        except Exception as e:

            raise CustomException(e, sys)

