from bs4 import BeautifulSoup
import urllib.request
import re
from itertools import chain



seed_url = "https://www.sec.gov/news/pressreleases"


urls = [seed_url]    #queue of urls to crawl
seen = [seed_url]    #stack of urls seen so far
urls_charges = []    #queue of urls to crawl
opened = []
text = ['a']
text_urls = []
text_charges = []
n=-1


maxNumUrl = 20; #set the maximum number of urls to visit
print("Starting with url="+str(urls))
while len(urls) > 0 and len(urls_charges) < maxNumUrl and urls not in seen:
    try:
        n = n + 1
        curr_url=urls.pop(0)
        req = urllib.request.Request(curr_url,headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urllib.request.urlopen(req).read()
        opened.append(curr_url)
        lowercase_text = webpage.lower()






    except Exception as ex:
        print("Unable to access= "+curr_url)
        print(ex)
        continue    #skip code below

    soup = BeautifulSoup(lowercase_text)  # creates object soup
    searched_word = 'charges'
    results = soup.body.find_all(string=re.compile('.*{0}.*'.format(searched_word)), recursive=True)
    if len(results) > 0 and curr_url not in urls_charges:
        urls_charges.append(curr_url)
        text_charges.append(text[n])




    for tag in soup.find_all('a', href = True): #find tags with links
        list = tag.text
        childUrl = tag['href'] #extract just the link
        o_childurl = childUrl
        childUrl = urllib.parse.urljoin('https://www.sec.gov/news/pressrelease/', childUrl)
        if 'https://www.sec.gov/news/pressrelease/' in childUrl and childUrl not in seen:
            urls.append(childUrl)
            seen.append(childUrl)
            text.append(list)


url_text=[]

#del urls_charges [0]
#del text_charges [0]

for i in range(len(urls_charges)):
    url_text.append([urls_charges[i], text_charges[i]])

del url_text[0]
print(url_text)

#print(urls_charges)
#print(text_charges)
#print(text)


