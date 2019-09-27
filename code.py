#!/usr/bin/env python
# coding: utf-8
from bs4 import BeautifulSoup
import requests
url="https://www.archlinux.org/"
source=requests.get(url)
soup=BeautifulSoup(source.text,'html')
title=soup.find('title')
print("this is with html tags :",title)
qwery=soup.find('h2')
print(qwery.text) 
links=soup.find('a')
colorcode=soup.find('#')
print(colorcode)

