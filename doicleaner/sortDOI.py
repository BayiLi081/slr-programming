import pandas as pd
import numpy as np
import os

def doi_exporter(data_path, file_name, col, export_path):
    
    data_path = data_path + file_name
    
    data = pd.read_csv(data_path)

    data = data.dropna(subset=[col[1]])

    data = data[col]

    doi = data[col]

    data.rename(columns={col[0]: 'id'}, inplace=True)

    data.rename(columns={col[1]: 'doi'}, inplace=True)

    doi.rename(columns={col[0]: 'id'}, inplace=True)

    doi.rename(columns={col[1]: 'doi'}, inplace=True)

    for x in ['doi.org/', 'https://', 'http://', 'doi:', 'DOI:', 'DOI ', 'doi ', 'DOI', 'doi']:
        doi.loc[doi['doi'].str.contains(x), 'doi'] = doi.loc[doi['doi'].str.contains(x), 'doi'].str.replace(x, '')

    txt_path = data_path.replace(file_name, 'doi.txt')
    
    doi.to_csv(txt_path, index=False, header=False)

    txt_path = data_path.replace(file_name, 'pure_doi.txt')
    
    doi['doi'].to_csv(txt_path, index=False, header=False)

    data = pd.read_csv(data_path)
    data.rename(columns={col[0]: 'id'}, inplace=True)
    data = data.merge(doi, on='id', how='left')
    
    # remove '.csv' from file_name
    file_name = file_name[:-4]
    newdata_path = data_path.replace(file_name, f'{file_name}_wdoi')

    data.to_csv(newdata_path, index=False)

if __name__ == "__main__":
    data_path = 'data/sample-data/'
    file_name = 'savedrecs.csv'
    export_path = 'data/collection/PDFs/'
    col = ['UT (Unique WOS ID)', 'DOI']
    doi_exporter(data_path, file_name, col, export_path)
# %%
