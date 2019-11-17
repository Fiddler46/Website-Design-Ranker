import urllib.request as req
from bs4 import BeautifulSoup
import re
count = 0

filepath = 'urls.txt'
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        print(line)
        url = line
        html = req.urlopen(line) # request the initial page
        soup = BeautifulSoup(html, 'html.parser')
        for styles in soup.select('style'): # get in-page style tags
            try:
                regex = r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})'
                result = re.findall(regex, styles.string)
                #print((set(result)))
                #print(len(set(result)))
            except:
                print("Error in ins")
                pass
            count = count + len(set(result))
        for link in soup.find_all('link', type='text/css'): # get links to external style sheets
            try:
                address = link['href'] # the address of the stylesheet
                #if address.startswith('/'): # relative link
                add = url + address
                #print(add)
                css = req.urlopen(add).read() # make a request to download the stylesheet from the address
                #print(css)
                regex = r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})'
                result = re.findall(regex, css.decode('utf-8'))
                #print((set(result)))
                #print(len(set(result)))
                count = count + len(set(result))
            except:
                print("Error")
                pass
        print(count)

