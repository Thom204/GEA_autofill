import pandas as pd

def get(key):
    id = df[df['EMAIL'] == (key+'@unal.edu.co')]['NÚMERO ASIGNADO']
    return (False if id.empty else id.values[0])

def details(key):
    det = df[df['EMAIL'] == (key+'@unal.edu.co')]['NOMBRE COMPLETO']
    return det.values[0]

df = pd.read_csv('Lista_CI.csv')