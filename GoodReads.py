import urllib
from BeautifulSoup import *
import re
import requests
giveawaySub = {"Username":"wearbros@gmail.com", "Password":"12345"}
html = raw_input("Enter URL")
url = urllib.urlopen(html)
file = url.read()
soup = BeautifulSoup(file)
tags = soup("a")
giveaway = list()
for tag in tags:
    giveaway.append(tag.get("href",None))
x = list()
for iteam in giveaway:
    if re.search("(/giveaway/enter_choose_address.*)", iteam):
        x.append(iteam)
for links in x:
    url = urllib.urlopen("https://www.goodreads.com"+links)
    soup = BeautifulSoup(url.read())
    tag = soup("a")
    
