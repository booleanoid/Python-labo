#encoding:utf-8
#get Yahoo auction items

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getItemList(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'html5lib')

        list = bsObj.find("div", id="list01").table
        item_list = list.find_all("tr")

        id_num = 1
        for i in item_list:
            h3 = i.find("h3")
            if h3:
                print('id:%d' % id_num)
                item_name = h3.a.string

                exhibitor = i.find("div", class_="sinfwrp").find_all("a")[1].string
                price_now = i.find("td", class_="pr1").text

                print('item_name:%s' % item_name)
                print('exhibitor:%s' % exhibitor)
                print('price now:%s' % price_now)
                print("--------------------------------------------------")
                id_num += 1


    except AttributeError as e:
        return None
    return item_list


def getCsv(url):
    item_list_results = []

    bs = getItemList(url)
    for b in bs:
        print(b)

getItemList("https://auctions.yahoo.co.jp/category/list/2084236857/?tab_ex=commerce&auccat=2084236857")

