from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import pandas as pd
import requests

option = webdriver.ChromeOptions()
option.add_argument('--headless')

driver = webdriver.Chrome(service = Service("C:/Users/lelaj/Downloads/chromedriver_win32/chromedriver"), options = option)

driver.get('http://stats.ncaa.org/player/index?id=15940&org_id=756&stats_player_seq=1973760&year_stat_category_id=14961') 

soup = BeautifulSoup(driver.page_source, 'html.parser') 
 
table = soup.select("#game_breakdown_div")
ips = soup.select("#game_breakdown_div tr td")

huh = pd.read_html(requests.get("http://stats.ncaa.org/player/index?id=15940&org_id=756&stats_player_seq=1973760&year_stat_category_id=14961", headers = {'User-agent': 'Mozilla/5.0'}).text)

print(huh)