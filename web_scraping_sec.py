import requests
import bs4
import pandas as pd

sic_codes = [1311]
#sic_codes = [1381, 1382, 1389, 1311] #1381-52, 1382 - 12, 1389 - 28, 1311 - 282
typ = "CORRESP" #UPLOAD
frm_date = "01/01/2019" #mm/dd/yyyy
to_date = "09/07/2020"  #mm/dd/yyyy
#link = "https://searchwww.sec.gov/EDGARFSClient/jsp/EDGAR_MainAccess.jsp?search_text=*&sort=Date&formType=Form" + typ + "&isAdv=true&stemming=true&numResults=100&querySic={}&fromDate=" + frm_date + "&toDate=" + to_date + "&numResults=100"
link = "https://searchwww.sec.gov/EDGARFSClient/jsp/EDGAR_MainAccess.jsp?search_text=*&sort=Date&startDoc={0}&numResults=100&isAdv=true&formType=Form" + typ + "&fromDate=" + frm_date + "&toDate=" + to_date + "&stemming=true&querySic={1}"

linkdata = pd.DataFrame()
filelinks = []
company_name = []
datelist = []
letter_type = []

for code in sic_codes:
    startdoc = 1
    while True:    
        res = requests.get(link.format(startdoc, code))
        soup = bs4.BeautifulSoup(res.text,'lxml')
        filings = soup.select('.filing')                #selecting all filing class elements <..class = 'filing'..>
        dates = soup.findAll('i', {'class' : 'blue'})   #selecting all i with class blue <i, class = 'blue'>(dates format for the website)
        
        if len(filings) == 0:
            break
        
        for filing in filings:
            filelinks.append(str(filing['href']).split('\'')[1])        #extracting links from filings class elements
            company_name.append(str(filing.text).split(' for ')[1])     #extracting company from filings class elements
            letter_type.append(str(filing.text).split(' for ')[0])      #extracting type from filings class elements
            
        for date in dates:
            datelist.append(str(date.text))                             #extracting dates from <i, class = 'blue'> element
        
        startdoc = startdoc + 100

linkdata['File link'] = filelinks
linkdata['Company'] = company_name
linkdata['Type'] = letter_type
linkdata['Date'] = datelist

linkdata.to_excel('linkdata-CORRESP-{}.xlsx'.format(sic_codes[0]), index = False)
