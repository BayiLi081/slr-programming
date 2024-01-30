#%%
import pandas as pd
import numpy as np
import os

#%%
def clean(data_path, file_name, summary_path, summary_name):
    
    data_path = data_path + file_name
    summary_path = summary_path + summary_name
    
    data = pd.read_csv(data_path)
    summary = pd.read_csv(summary_path)

    new_path = summary_path.replace(summary_name, file_name)

    data = data.merge(summary, left_on='doi', right_on='DOI', how='left')

    data.to_csv(new_path, index=False)

if __name__ == "__main__":
    data_path = '../data/sample-data/'
    file_name = 'savedrecs_wdoi.csv'
    summary_path = '../data/collection/PDFs/'
    summary_name = 'result.csv'
    clean(data_path, file_name, summary_path, summary_name)
# %%
