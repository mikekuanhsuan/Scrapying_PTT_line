
import requests
import re
import time
from bs4 import BeautifulSoup
from typing import Optional, Tuple

class PttMacShopScraper:
    def __init__(self, lineToken: str):
        self.lineToken = lineToken
        self.ptt_site = 'https://www.ptt.cc/bbs/MacShop/index.html'
        self.today = self._get_today()

    def _get_today(self) -> str:
        todayMonth = int(time.strftime('%m'))
        todayDay = time.strftime('%d')
        today = f'{todayMonth:02}/{todayDay}'
        return today

    def _get_last_page(self) -> int:
        indexRes = requests.get(self.ptt_site)
        indexSoup = BeautifulSoup(indexRes.text, 'html.parser')
        pages = indexSoup.find('a', text=re.compile('上頁'))['href']
        last_page = int(re.findall('\d+', pages)[0])
        return last_page

    def scrape(self) -> None:
        last_page = self._get_last_page()
        for p in range(last_page+1, last_page - 2, -1 ):
            url = f'https://www.ptt.cc/bbs/MacShop/index{p}.html'
            res = requests.get(url)
            if res.status_code == requests.codes.ok:
                self._parse_page(res.text)

    def _parse_page(self, page: str) -> None:
        soup = BeautifulSoup(page, 'html.parser')
        stories = soup.find_all('div', class_ = 'r-ent')
        for s in stories:
            if s.find('div', 'date').string.strip() == self.today and s.find('a', text = re.compile(r'[販售](.*)watch(.*)', re.I)):
                self._process_story(s)

    def _process_story(self, story) -> None:
        if story.find('a'):
            href = story.find('a')['href']
            title = story.find('a').text
            date = story.find('div','date').text.strip()
            print(f'https://www.ptt.cc{href}', title, date)
            botText = (f'https://www.ptt.cc{href}\n{title}', date)
            lineTool.lineNotify(self.lineToken, botText)

if __name__ == "__main__":
    lineToken = '<Your Line Notify Token>'
    scraper = PttMacShopScraper(lineToken)
    scraper.scrape()
