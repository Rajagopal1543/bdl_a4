import pandas as pd
from zipfile import ZipFile
import os
import yaml

def process():

    truelocdir = os.path.dirname(__file__)
   
    with open(truelocdir+'/myParams.yaml', 'r') as file:
        myParams = yaml.safe_load(file)
    #print(truelocdir)
    data = pd.read_csv(os.path.join(truelocdir,'newweather', myParams['file_name']))

    data['DATE'] = pd.to_datetime(data['DATE'])
    data['Month'] = data['DATE'].dt.month
    monthlyValues = data.groupby('Month')[myParams['field_name']].mean()
    monthlyValues.to_csv(truelocdir+'/CalculatedMonthly.csv', index=False)

process()
