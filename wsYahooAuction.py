from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from pprint import pprint
from datetime import datetime as dt
import pandas as pd
import time


class WsYahooAuction():
    def __init__(self):
        self.url = ""

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url

    def get_bs_obj(self):
        try:
            html = urlopen(self.url)
        except HTTPError as e:
            print(e)
            return None
        return BeautifulSoup(html.read(), 'html5lib')

    def get_item_list(self):
        try:
            item_list = []

            while True :
                bs_obj = self.get_bs_obj()
                list_elm = bs_obj.find("div", id="list01").table
                next_link_elm = bs_obj.find("div", id="ASsp1").find("p", class_="next")
                next_link = next_link_elm.a.get("href") if next_link_elm.a else None

                for i in list_elm.find_all("tr"):
                    h3 = i.find("h3")
                    if h3:
                        item_name = h3.a.string
                        item_url = h3.a.get('href')
                        exhibitor = i.find("div", class_="sinfwrp").find_all("a")[1].string
                        price_now = i.find("td", class_="pr1")
                        price_now.ul.decompose()
                        price_now = price_now.get_text().replace(" ", "").replace("\n", "")
                        price_prompt_decision = i.find("td", class_="pr2").text
                        remaining_time = i.find("td", class_="ti").text
                        item_url_split = item_url.split('/')
                        id = item_url_split[5]

                        item_list.append([id, item_name, exhibitor, price_now, price_prompt_decision, remaining_time])

                if next_link is None:
                    break
                else:
                    self.url = next_link
                    time.sleep(2)

            # pprint(item_list)

        except AttributeError as e:
            return None
        return item_list

    def write_csv(self, item_name, item_list):
        tdatetime = dt.now()

        # fetched_dataframes
        df = pd.DataFrame(item_list)
        df.to_csv('Yahoo_auction_list_%s_%d-%d-%d.csv' % (item_name, tdatetime.year, tdatetime.month, tdatetime.day))
        print('%s Success!!' % item_name)

obj = WsYahooAuction()
obj.set_url("https://auctions.yahoo.co.jp/category/list/2084236857/?tab_ex=commerce&auccat=2084236857")
obj.write_csv('ES-335', obj.get_item_list())
