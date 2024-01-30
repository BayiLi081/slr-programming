#%%
import pandas as pd
import numpy as np
import os

#%%
def clean(data_path, file_name, pdf_path):
    
    data_path = data_path + file_name
    # get all the pdfs (ends with '.pdf') in the pdf_path
    pdfs = [pdf for pdf in os.listdir(pdf_path) if pdf.endswith('.pdf')]
    
    data = pd.read_csv(data_path)

    pdfs_data = data['PDF Name'].tolist()

    # drop the rows with no pdfs
    pdfs_data = [pdf for pdf in pdfs_data if str(pdf) != 'nan']

    if len(pdfs_data) != len(pdfs):
        print('Check the number of PDFs and the number of PDFs in the data')
        print(f'Number of PDFs: {len(pdfs)}')
        print(f'Number of PDFs in the data: {len(pdfs_data)}')
    for pdf in pdfs:
        if pdf not in pdfs_data:
            print(pdf)

    # remove the rows with no pdfs
    data_cleaned = data.dropna(subset=['PDF Name'])

    print(data_cleaned)



    # rename pdfs in the pdf_path use the id column from data_cleaned
    for index, row in data_cleaned.iterrows():
        old_name = row['PDF Name']
        new_name = row['id']
        os.rename(pdf_path + old_name, pdf_path + new_name+'.pdf')


    data = data.merge(summary, left_on='doi', right_on='DOI', how='left')

    data.to_csv(new_path, index=False)

if __name__ == "__main__":
    data_path = '../data/collection/'
    file_name = 'savedrecs_wdoi.csv'
    pdf_path = '../data/collection/PDFs/'
    clean(data_path, file_name, pdf_path)
# %%
