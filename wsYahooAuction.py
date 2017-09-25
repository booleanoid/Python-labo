#encoding:utf-8
#get Yahoo auction items

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from pprint import pprint
import time



def get_bs_obj(url):
    try:
        html = urlopen(url)
        bs_obj = BeautifulSoup(html.read(), 'html5lib')
    except HTTPError as e:
        print(e)
        return None
    return bs_obj

def get_item_list(url):
    try:
        item_list = []
        id_num = 1
        page_num = 1
        while True :
            bsObj = get_bs_obj(url)
            listEml = bsObj.find("div", id="list01").table
            next_link_elm = bsObj.find("div", id="ASsp1").find("p", class_="next")
            next_link = next_link_elm.a.get("href") if next_link_elm.a else None

            for i in listEml.find_all("tr"):
                h3 = i.find("h3")
                if h3:
                    item_name = h3.a.string
                    exhibitor = i.find("div", class_="sinfwrp").find_all("a")[1].string
                    price_now = i.find("td", class_="pr1")
                    price_now.ul.decompose()
                    price_now = price_now.get_text().replace(" ", "").replace("\n", "")
                    price_prompt_decision = i.find("td", class_="pr2").text
                    item_list.append([id_num, item_name, exhibitor, price_now, price_prompt_decision])

                    id_num += 1

            if next_link is None:
                break
            else:
                page_num += 1
                url = next_link
                time.sleep(2)

        pprint(item_list)

    except AttributeError as e:
        return None
    return item_list


def get_csv(url):
    item_list_results = []

    bs = getItemList(url)
    for b in bs:
        print(b)

get_item_list("https://auctions.yahoo.co.jp/category/list/2084236857/?tab_ex=commerce&auccat=2084236857")

