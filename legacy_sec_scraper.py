from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from random import randint

#url = "https://www.sec.gov/cgi-bin/srch-edgar?text=ASSIGNED-SIC%3D1389+AND+form-type%3DUPLOAD&first=2000&last=2006"
url = "https://www.sec.gov/cgi-bin/srch-edgar?text=ASSIGNED-SIC%3D%281311%20OR%201381%20OR%201382%20OR%201389%29%20AND%20%20form-type%3D%28UPLOAD%2A%20OR%20CORRESP%2A%29&start={}&count=80&first=2000&last=2006"

start = 1 #<start = start + 80, while start is 1865>
linkdata = pd.DataFrame()
filelinks = []
company_name = []
datelist = []
letter_type = []

def set_sleep_timer(time_upper_limit):
    sleep_time = randint(0, int(time_upper_limit))
    print("\nSleeping for " + str(sleep_time) + " seconds.")
    time.sleep(sleep_time)
 
while start < 1865: 
    set_sleep_timer(randint(2,6))
    
    res = requests.get(url.format(start))
    soup = BeautifulSoup(res.text, 'lxml')
    
    rows = soup.select('tr') #rows[12] to rows[92] are letters
    
    for i in range(12,93):
        company = rows[i].select('td')[1].text
        if company != 'Modified: 06/05/2012':
            link = "https://www.sec.gov/" + rows[i].select('td')[2].select('a')[0]['href']
            typ = rows[i].select('td')[3].text
            date = rows[i].select('td')[4].text
            
            company_name.append(company)
            filelinks.append(link)
            letter_type.append(typ)
            datelist.append(date)
    start = start + 80
   
linkdata['File link'] = filelinks
linkdata['Company'] = company_name
linkdata['Type'] = letter_type
linkdata['Date'] = datelist

linkdata.to_excel("2000-2006-Master-linkdata.xlsx",index = False)