import lxml.html
from lxml.cssselect import CSSSelector
import requests
r = requests.get('http://google.com')
tree = lxml.html.fromstring(r.text)
print (lxml.html.tostring(tree))
sel = CSSSelector('a')
results = sel(tree)
print (results)