import requests
import lxml.html
from lxml import etree

tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())

ul = tree.findall('/body/div[2]/div[2]/div[5]/main/section[2]/div[3]/div[1]/div[3]/div[1]/div/div/article/div[2]/ul/li[1]')

for li in ul:
    a = li.find('a')
    print(a.text)