import csv
import requests
import math
from random import randrange

# URLs dos datasets
url_wine = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'
url_iris = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Função para carregar o dataset Wine da UCI
def load_wine_data(url):
    response = requests.get(url)
    decoded_content = response.content.decode('utf-8').splitlines()
    dataset = list(csv.reader(decoded_content))
    for i in range(len(dataset[0])):
        for row in dataset:
            row[i] = float(row[i]) if i != 0 else int(row[i])
    return dataset

# Função para carregar o dataset IRIS da UCI
def load_iris_data(url):
    response = requests.get(url)
    decoded_content = response.content.decode('utf-8').splitlines()
    dataset = list(csv.reader(decoded_content))
    dataset = [row.split(",") for row in dataset if row]
    for i in range(len(dataset[0])):
        for row in dataset:
            row[i] = float(row[i]) if i != 4 else row[i]
    return dataset

# Processar dataset IRIS
def process_iris_data(url):
    iris_data = load_iris_data(url)
    for row in iris_data:
        if row[-1] == 'Iris-setosa':
            row[-1] = 0
        elif row[-1] == 'Iris-versicolor':
            row[-1] = 1
        elif row[-1] == 'Iris-virginica':
            row[-1] = 2
    return iris_data

# Função para dividir o dataset
def test_split(index, value, dataset):
    left, right = [], []
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right
