import pandas as pd
import time
from random import randint

def set_sleep_timer(time_upper_limit):
    sleep_time = randint(0, int(time_upper_limit))
    print("\nSleeping for " + str(sleep_time) + " seconds.")
    time.sleep(sleep_time)
    
#sic_codes = [1381]
#sic_codes = [1381, 1382, 1389, 1311]
#typ = ['UPLOAD','CLU']
#typ = ['CORRESP','CLC']
#linkdata = pd.read_excel('2000-2006-linkdata-{0}-{1}.xlsx'.format(typ[0], sic_codes[0]))
linkdata = pd.read_excel('latest_file_list_sec.xlsx')
i = 0
#linkdata = linkdata[linkdata['Type'] == typ[0]]

linkdata['File'] = '.\\Legacy_rem\\' + linkdata['Company'].str.replace('/', '_', regex = False) + "_" + linkdata['Type'] +  "_" + linkdata['Date'].str.replace('/', '_', regex = False)
linkdata['Copy'] = linkdata.groupby('File ').cumcount()
linkdata['Copy'] = "_" + linkdata['Copy'].astype('str')
linkdata['Copy'] = linkdata['Copy'].replace("_0","")
linkdata['Filename'] = linkdata['File'] + linkdata['Copy'] + ".txt"

from pathlib import Path
import requests
   
for index, row in linkdata.iterrows():        
    filename = Path(row['Filename'])
    url = row['File link']
    response = requests.get(url)
    filename.write_bytes(response.content)    
    
    i = i + 1
    if i % 50 == 0:
        print("50 files downloaded: Going to sleep mode for 20 secs")
        set_sleep_timer(30)


'''
if typ[0] == 'UPLOAD':
    from pathlib import Path
    import requests
        
    for index, row in linkdata.iterrows():        
        filename = Path(row['Filename'])
        url = row['File link']
        response = requests.get(url)
        filename.write_bytes(response.content)    
        
        i = i + 1
        if i % 50 == 0:
            print("50 files downloaded: Going to sleep mode for 20 secs")
            time.sleep(20)
    
    filename = Path(linkdata['Filename'][0])
    url = linkdata['File link'][0]
    response = requests.get(url)
    filename.write_bytes(response.content)
    
    
if typ[0] == 'CORRESP':
    import pdfkit
    
    for index,row in linkdata.iterrows():        
        pdfkit.from_url(row['File link'], row['Filename'])
        
        i = i + 1
        if i % 50 == 0:
            print("50 files downloaded: Going to sleep mode for 20 secs")
            time.sleep(20)
        
    
    pdfkit.from_url(linkdata['File link'][0], linkdata['Filename'][0])
    
'''