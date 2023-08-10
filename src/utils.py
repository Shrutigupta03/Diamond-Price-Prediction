import os
import sys
import pickle
import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging

from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        logging.info('Exception occured while saving pickle file')
        raise CustomException(e, sys)

def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        for i in range(len(models)):
            model=list(models.values())[i]
            # Train Model
            model.fit(X_train, y_train)

            # Predict on Test Data
            y_test_pred = model.predict(X_test)

            # Get R2 scores for train & test data
            # train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        logging.info('Exception occured while evaluating model')
        raise CustomException(e, sys)