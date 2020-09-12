from bs4 import BeautifulSoup
import pandas as pd
import urllib
import ssl
import time
from random import randint

reviews_df = pd.DataFrame()
review_list = []
title_list = []
rating_list = []

def set_sleep_timer(time_upper_limit):
    sleep_time = randint(0, int(time_upper_limit))
    print("\nSleeping for " + str(sleep_time) + " seconds.")
    time.sleep(sleep_time)

url = "https://www.amazon.in/Abro-Colour-Spray-Paint-400ml/product-reviews/B00T7THCJ2/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={}"
page = 1
#Total 294 pages of review for our product
while page < 295:
    ssl._create_default_https_context = ssl._create_unverified_context
    #Amazon blocks direct requests, adding agent to fool
    user_agent = 'Mozilla/5.0'
    headers = {'User-Agent' : user_agent}
    values = {}
    
    #sleepnig the system for random time to avoid IP lock
    set_sleep_timer(randint(2,9))
    
    data = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(url.format(page), data, headers)
    response = urllib.request.urlopen(req)
    html = response.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    review = soup.select(".a-size-base.review-text.review-text-content")
    review_title = soup.select(".a-size-base.review-title.a-text-bold")
    rating = soup.select(".a-icon-alt")
    #Ignoring first 2 titles in page, and irst three reviews (Critical/Helpful reviews and Total ratings)
    
    for i in range(len(review)):
        review_list.append(review[i].text)
        title_list.append(review_title[i+2].text)
        rating_list.append(rating[i+3].text)
    page = page + 1

reviews_df['Title'] = title_list
reviews_df['Rating'] = rating_list
reviews_df['Review'] = review_list

reviews_df.to_excel('Abro-Colour-Spray-Paint_reviews.xlsx', index = False)