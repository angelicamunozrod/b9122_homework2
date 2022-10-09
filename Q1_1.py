import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

from bs4 import BeautifulSoup
import urllib.request
import re

seed_url = "https://www.federalreserve.gov/newsevents/pressreleases.htm"

urls = [seed_url]    #queue of urls to crawl
seen = [seed_url]    #stack of urls seen so far
urls_covid = []    #queue of urls to crawl
opened = []

maxNumUrl = 10; #set the maximum number of urls to visit
print("Starting with url="+str(urls))
while len(urls) > 0 and len(urls_covid) < maxNumUrl and urls not in seen:
    try:
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

    searched_word = 'covid'
    results = soup.body.find_all(string=re.compile('.*{0}.*'.format(searched_word)), recursive=True)
    if len(results) > 0 and curr_url not in urls_covid:
        urls_covid.append(curr_url)


    for tag in soup.find_all('a', href = True): #find tags with links
        childUrl = tag['href'] #extract just the link
        o_childurl = childUrl
        childUrl = urllib.parse.urljoin(seed_url, childUrl)
        if seed_url in childUrl and childUrl not in seen:
            urls.append(childUrl)
            seen.append(childUrl)
        else:
            urls.append(childUrl)
            seen.append(childUrl)



print(urls_covid)






