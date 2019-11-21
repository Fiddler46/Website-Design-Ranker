<<<<<<< HEAD
<<<<<<< HEAD
import scrapy
=======
import urllib.request as req
from bs4 import BeautifulSoup
>>>>>>> 810b893ac3b8d239a02f1afc7c29528f50018ff1
=======
>>>>>>> fcddf4d7f489085668c212297db6be855fa7cf14
import re

import requests
from bs4 import BeautifulSoup

REGEX_CSS = re.compile(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})')

def main():
    base_url = input('Enter a full website address: ')
    # Do verification here

    html = requests.get(base_url) # request the initial page
    soup = BeautifulSoup(html.text, 'html.parser')
    for styles in soup.select('style'): # get in-page style tags
        print('in page style:')
        print(styles.string)

<<<<<<< HEAD
<<<<<<< HEAD
    print(result)
=======
    css_urls = map(
    lambda u: base_url + u if u.startswith("/") else u,
    (l["href"] for l in soup.find_all('link', type='text/css') if l.get("href"))
)
    for url in css_urls:
        css_request = requests.get(url)
>>>>>>> fcddf4d7f489085668c212297db6be855fa7cf14

        if css_request.status_code != 200:
            print("Could not fetch CSS!")
            continue
        result = REGEX_CSS.findall(css_request.text)
        if not result:
            print("Pattern not found in CSS!")
            continue
        print((set(result)))
        print(len(set(result)))

<<<<<<< HEAD
=======
    print((set(result)))
    print(len(set(result)))
>>>>>>> 810b893ac3b8d239a02f1afc7c29528f50018ff1
    
=======
if __name__ == "__main__":
    main()
>>>>>>> fcddf4d7f489085668c212297db6be855fa7cf14
