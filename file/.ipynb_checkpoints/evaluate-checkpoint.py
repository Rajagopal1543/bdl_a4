from sklearn.metrics import r2_score
import pandas as pd
import os

def evaluate():
    truelocdir = os.path.dirname(__file__)

    ActualMonthly = pd.read_csv(truelocdir+'/ActualMonthly.csv')
    CalculatedMonthly = pd.read_csv(truelocdir+'/CalculatedMonthly.csv')
    if len(ActualMonthly) != len(CalculatedMonthly):
        if len(ActualMonthly) <= len(CalculatedMonthly):
            CalculatedMonthly = CalculatedMonthly[:len(ActualMonthly)]
           
        else:
             ActualMonthly = ActualMonthly[:len(CalculatedMonthly)]
    r2 = r2_score(ActualMonthly, CalculatedMonthly)
    if r2 >= 0.9:
        print('Consistent Dataset')
    else:
        print('Inconsistent Dataset')
    return r2

evaluate()
