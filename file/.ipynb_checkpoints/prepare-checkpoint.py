import pandas as pd
from zipfile import ZipFile
import os

def prepare():
    truelocdir = os.path.dirname(__file__)

    with ZipFile(truelocdir+'/weatherdata.zip', 'r') as zObject: 
        zObject.extractall(path=os.path.join(truelocdir,'newweather')) 

    #files = os.listdir(truelocdir)
    files = os.listdir(os.path.join(truelocdir,'newweather'))
    #files = [file for file in files if file.endswith(').csv')]
    files = [file for file in files]
    #print(files)
    #files=[files[2]]
    file_name = ''
    #print(files)
    for f in files:
        data = pd.read_csv(os.path.join(truelocdir,'newweather',f),low_memory=False)
        if data['MonthlyDepartureFromNormalAverageTemperature'].isnull().sum() < len(data['MonthlyDepartureFromNormalAverageTemperature']) and data['DailyDepartureFromNormalAverageTemperature'].isnull().sum() < len(data['DailyDepartureFromNormalAverageTemperature']):
            file_name = f 
            #print(file_name)
            field_name = 'DailyDepartureFromNormalAverageTemperature'
            with open(truelocdir+'/myParams.yaml', 'w') as file:
                file.write(f'file_name: {file_name}\n')
                file.write(f'field_name: {field_name}\n')
      
  
            ActualMonthly = data['MonthlyDepartureFromNormalAverageTemperature']
            ActualMonthly.dropna(inplace=True)

            ActualMonthly.to_csv(truelocdir+'/ActualMonthly.csv', index=False)

prepare()
