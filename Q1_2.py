from bs4 import BeautifulSoup
import urllib.request
import re

seed_url = "https://www.sec.gov/news/pressreleases"


urls = [seed_url]    #queue of urls to crawl
seen = [seed_url]    #stack of urls seen so far
urls_charges = []    #queue of urls to crawl
opened = []
matrix = []


maxNumUrl = 20; #set the maximum number of urls to visit
print("Starting with url="+str(urls))
while len(urls) > 0 and len(urls_charges) < maxNumUrl and urls not in seen:
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

    searched_word = 'charges'

    results = soup.body.find_all(string=re.compile('.*{0}.*'.format(searched_word)), recursive=True)
    if len(results) > 0 and curr_url not in urls_charges:
        urls_charges.append(curr_url)



    for tag in soup.find_all('a', href = True): #find tags with links
        list = tag.text
        childUrl = tag['href'] #extract just the link
        o_childurl = childUrl
        childUrl = urllib.parse.urljoin('https://www.sec.gov/news/pressrelease/', childUrl)
        if 'https://www.sec.gov/news/pressrelease/' in childUrl and childUrl not in seen:
            urls.append(childUrl)
            seen.append(childUrl)
            matrix.append([list, childUrl])



#del matrix[:2]
print(matrix[2:22])


