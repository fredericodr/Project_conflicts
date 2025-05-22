import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

<<<<<<< HEAD
def clean_data(df):
    df.columns = [col.lower() for col in df.columns]
    return df
=======
def something_else(df):
    return df.clean()
>>>>>>> features
