import pandas as pd
import os

def load_data(filepath):
    if os.path.exists(filepath):
        return pd.read_csv(filepath)
    else:
        return pd.DataFrame()

def save_data(df, filepath):
    df.to_csv(filepath, index=False)
