

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


class WebScraping():

    def get_wiki_link(self, url):
        html = urlopen(url)
        bsObj = BeautifulSoup(html)
        for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
            if 'href' in link.attrs:
                print(link.attrs['href'])


if __name__ == '__main__':
    obj = WebScraping()
    obj.get_wiki_link("https://en.wikipedia.org/wiki/Vulfpeck")
