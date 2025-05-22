import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def something_else(df):
    return df.clean()