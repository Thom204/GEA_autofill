import pandas as pd

def get(key):
    print(df.keys)
    id = df[df['gmail'] == (key+'@unal.edu.co')]['NÚMERO ASIGNADO']
    return (False if id.empty else id.values[0])

def details(key):
    det = df[df['gmail'] == (key+'@unal.edu.co')]['NOMBRES']
    return det.values[0]

df = pd.read_csv('Lista_CI.csv')