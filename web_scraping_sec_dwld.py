import pandas as pd

sic_codes = [1389]
#sic_codes = [1381, 1382, 1389, 1311]
#typ = ['UPLOAD','CLU']
typ = ['CORRESP','CLC']
linkdata = pd.read_excel('linkdata-{0}-{1}.xlsx'.format(typ[0], sic_codes[0]))

linkdata = linkdata[linkdata['Type'] == typ[0]]

linkdata['Filename'] = linkdata['Company'] + "_" + typ[1] +  "_" + linkdata['Date'].str.replace('/', '_', regex = False) + ".pdf"

if typ[0] == 'UPLOAD':
    from pathlib import Path
    import requests
        
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
    
if typ[0] == 'CORRESP':
    import pdfkit
    
    for index,row in linkdata.iterrows():        
        pdfkit.from_url(row['File link'], row['Filename'])
    '''
    pdfkit.from_url(linkdata['File link'][0], linkdata['Filename'][0])
    '''