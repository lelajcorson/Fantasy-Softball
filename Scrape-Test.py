from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import pandas as pd
import requests


url = requests.get("http://stats.ncaa.org/player/index?id=15940&org_id=756&stats_player_seq=1973760&year_stat_category_id=14961", headers = {"User-Agent" : "Mozilla/5.0"})

option = webdriver.ChromeOptions()
option.add_argument('--headless')
driver = webdriver.Chrome(service = Service("C:\Lela\Coding\chromedriver_win32\chromedriver"), options = option)

def getPlayerURL(name):
    driver.get("https://www.google.com/")
    driver.maximize_window()
    print(name)
    search = driver.find_element(By.XPATH, "//input[@type = 'text']")
    search.send_keys(name)

getPlayerURL("gabbie plain")
def getStats(url):
    tables = pd.read_html(url.text, match = "Schedule/Results")
    stats_table_temp = tables[1]
    stats_df = pd.DataFrame(stats_table_temp.values[2:], columns = stats_table_temp.iloc[1])
    print(stats_df)

# html_content = requests.get(url, headers = {'User-Agent': 'Chrome'}).text

# soup = BeautifulSoup(html_content, "lxml")
# #print(soup.prettify())

# gdp = soup.find_all("table")
# print(gdp)


# def getTable(url):
#     html_content = requests.get(url, headers = {'User-Agent': 'Chrome'}).text
#     soup = BeautifulSoup(html_content, "lxml")

#     big_div = soup.find(id = "game_breakdown_div") #the div containing the stats table
#     table = big_div.find("table", class_= "mytable") #the stats table
#     row_list = table.find_all("tr")
#     row_list.pop(0) #removing the title and links
    
    

#getTable(url)

# option = webdriver.ChromeOptions()
# option.add_argument('--headless')

# driver = webdriver.Chrome(service = Service("C:/Users/lelaj/Downloads/chromedriver_win32/chromedriver"), options = option)

# driver.get('http://stats.ncaa.org/player/index?id=15940&org_id=756&stats_player_seq=1973760&year_stat_category_id=14961') 

# soup = BeautifulSoup(driver.page_source, 'html.parser') 
 
# table = soup.select("#game_breakdown_div")
# ips = soup.select("#game_breakdown_div tr td")

# huh = pd.read_html(requests.get("http://stats.ncaa.org/player/index?id=15940&org_id=756&stats_player_seq=1973760&year_stat_category_id=14961", headers = {'User-agent': 'Mozilla/5.0'}).text)

# print(huh)