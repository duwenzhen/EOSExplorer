

from bs4 import BeautifulSoup
import urllib.request
import time
import random


site= 'https://etherscan.io/txs?a=0xd0a6e6c54dbc68db5db3a091b171a77407ff7ccf&p='
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

f = open('workfile', 'a')

for i in range(1167, 1947):
    req = urllib.request.Request(site + str(i), headers=hdr)
    page = urllib.request.urlopen(req)
    content = page.read()
    soup = BeautifulSoup(content, "html.parser")
    f.write(soup.find('tbody').text)
    print (i)
    #time.sleep(random.random())
