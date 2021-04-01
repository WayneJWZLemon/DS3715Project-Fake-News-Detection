import pandas as pd

pdFake = pd.read_csv('Kaggle-Clement-Bisaillon-Fake.csv')
print("Basic info about the fake news dataset from Clement Bisaillon")
pdFake.info()

pdTrue = pd.read_csv('Kaggle-Clement-Bisaillon-True.csv')
print("Basic info about the true news dataset from Clement Bisaillon")
pdTrue.info()
