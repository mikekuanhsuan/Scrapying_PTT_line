"# Scrapying_PTT_line" 

PttMacShopScraper
This Python script uses a web scraping technique to collect information about the most recent Apple Watch posts from PTT MacShop's last three pages and sends the relevant notifications via Line Notify.

Dependencies
This script depends on the following Python libraries:

requests
re
time
bs4 (BeautifulSoup)
lineTool (an external module for Line notifications)
Installation
To install the dependencies, run the following command:
pip install requests bs4


Note: The lineTool module should be properly installed or located in the same directory as the script.

Usage
The script can be run from the command line using Python 3:

python PttMacShopScraper.py

Before running, make sure to replace <Your Line Notify Token> in the script with your actual Line Notify Token:
  
  
  if __name__ == "__main__":
    lineToken = '<Your Line Notify Token>'  # replace with your token
    scraper = PttMacShopScraper(lineToken)
    scraper.scrape()

How it works
The script initializes a PttMacShopScraper object with a given Line Notify token. The scraper accesses the PTT MacShop web pages, extracts relevant post information and sends this information as a notification via Line Notify.
  
