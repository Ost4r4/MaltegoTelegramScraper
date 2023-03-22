from maltego_trx.entities import Alias
from maltego_trx.transform import DiscoverableTransform
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import re
import time

SLEEP_TIME = 2
scrolls_number = 10



class Maltego_Telegram_Scraper(DiscoverableTransform):
    @classmethod
    def create_entities(cls, request, response):
        identifier = request.Value
        try:
            names = cls.find_forwarders(identifier)
            if names:
                accounts_telegram = list(set(names))

                for username in accounts_telegram:
                    count = names.count(username)
                    response.addEntity(Alias, username)
            else:
                response.addUIMessage("No message posted or account does not exist")
        except IOError:
            response.addUIMessage("Unknown error")

    @staticmethod
    def find_forwarders(username):
        source_list = []
        target_list = []
        with Chrome() as driver:
            page_telegram = f'https://t.me/s/{username}'
            driver.get(page_telegram)
            time.sleep(SLEEP_TIME)

            last_height = driver.execute_script("return document.body.scrollHeight")
            for index_height in range(scrolls_number):
                driver.execute_script("window.scrollTo(0,-document.body.scrollHeight);")
                time.sleep(SLEEP_TIME)
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            forwarded_from_divs = soup.find_all("div", class_='tgme_widget_message_forwarded_from accent_color')
            for forwarded_from_div in forwarded_from_divs:
                forwarded_from_div_str = str(forwarded_from_div)
                if 'from_author' not in forwarded_from_div_str:
                    a_tag = forwarded_from_div.a
                    if a_tag:
                        href = a_tag.get('href')
                        if href:
                            forwarded_usernamename = re.sub('https://t.me/', '', href)
                            slash = forwarded_usernamename.find('/')
                            forwarded_usernamename = forwarded_usernamename[:slash]
                            source_list.append(username)
                            target_list.append(forwarded_usernamename)

            transit_links = soup.find_all("a", class_='tgme_widget_message_forwarded_from_name')
            for transit_link in transit_links:
                href = transit_link.get('href')
                if href:
                    forwarded_usernamename = re.sub('https://t.me/', '', href)
                    slash = forwarded_usernamename.find('/')
                    forwarded_usernamename = forwarded_usernamename[:slash]
                    source_list.append(username)
                    target_list.append(forwarded_usernamename)

        return target_list

if __name__ == "__main__":
    print(Maltego_Telegram_Scraper.find_forwarders('Dumpforums'))
