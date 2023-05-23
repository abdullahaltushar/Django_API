from django.shortcuts import render
from django.http import HttpResponse
import csv
import numpy as np
import pandas as pd
import requests
from sklearn.preprocessing import MinMaxScaler


# Create your views here.
def user_api(request):
    data = pd.read_csv('static/sale.csv', parse_dates=['date'])
    # add new line
    # define the number of days to use for the input sequence
    seq_length = 30
    X_train, y_train, X_test, y_test, scaler = prepare_data(data, seq_length)
    # URL of the API endpoint on the host machine
    api_url = "http://127.0.0.1:8000/api/h/"
    # Make a GET request to the API endpoint
    response = requests.get(api_url)

    # Process the response data
    if response.status_code == 200:
        model = response.json()
        return HttpResponse("success")
    else:
        return HttpResponse(" is not able")


def load_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        rows = [row for row in reader]
    return rows

# create supervised learning data
# prepare the data for training the model


def prepare_data(data, seq_length):
    # convert the data to a numpy array
    data = data[['Amount', 'Rate', 'Qty']].values
    # scale the data between 0 and 1
    scaler = MinMaxScaler()
    data = scaler.fit_transform(data)
    # create the input and output data
    X = []
    y = []
    for i in range(seq_length, len(data)):
        X.append(data[i-seq_length:i])
        y.append(data[i])
    X = np.array(X)
    y = np.array(y)
    # split the data into training and testing sets
    split = int(0.8*len(data))
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]
    return X_train, y_train, X_test, y_test, scaler
