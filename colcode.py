import urllib.request as req
from bs4 import BeautifulSoup
import re
url = input('enter a full website address: ')

html = req.urlopen(url) # request the initial page
soup = BeautifulSoup(html, 'html.parser')
for styles in soup.select('style'): # get in-page style tags
    print('in page style:')
    print(styles.string)

for link in soup.find_all('link', type='text/css'): # get links to external style sheets
    address = link['href'] # the address of the stylesheet
    if address.startswith('/'): # relative link
        address = url + address
    css = req.urlopen(address).read() # make a request to download the stylesheet from the address
    print('linked stylesheet')
    print(css)
with open('style.css') as f:
    file_contents = f.read()
    regex = r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})'
    result = re.findall(regex, file_contents)

    print((set(result)))
    print(len(set(result)))
    
