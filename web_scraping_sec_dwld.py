from pathlib import Path
import requests
import pandas as pd

linkdata = pd.read_excel('linkdata1381.xlsx')
typ = ['UPLOAD','CLU']
#typ = ['CORRESP','CLC']
linkdata = linkdata[linkdata['Type'] == typ[0]]

linkdata['Filename'] = linkdata['Company'] + "_" + typ[1] +  "_" + linkdata['Date'].str.replace('/', '_', regex = False) + ".pdf"

for index, row in linkdata.iterrows():
    
    filename = Path(row['Filename'])
    url = row['File link']
    response = requests.get(url)
    filename.write_bytes(response.content)

'''
filename = Path(linkdata['Filename'][0])
url = linkdata['File link'][0]
response = requests.get(url)
filename.write_bytes(response.content)
'''
