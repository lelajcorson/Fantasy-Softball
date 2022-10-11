from asyncio.windows_events import NULL
from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
from functools import wraps
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import pandas as pd
import requests
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from profiles import UserProfile, PlayerProfile

#setting up Flask
app = Flask(__name__)

url = requests.get("http://stats.ncaa.org/player/index?id=15940&org_id=756&stats_player_seq=1973760&year_stat_category_id=14961", headers = {"User-Agent" : "Mozilla/5.0"})

option = webdriver.ChromeOptions()
option.add_argument('--headless')
driver = webdriver.Chrome(service = Service("C:\Lela\Coding\chromedriver_win32\chromedriver"), options = option)


def get_player_URL(name):
    driver.get("http://stats.ncaa.org/search/players")
    #print(name)
    search = driver.find_element(By.XPATH, "//input[@type = 'search']")
    search.send_keys(name)

    delay = 10 # seconds
    try: #waiting for the page to load the search results
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="people_search_data_table"]/tbody/tr/td[1]/a')))
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")

    try:
        player_link = driver.find_element(by = By.LINK_TEXT, value = name.title())
    except Exception:
        print("Exception!")
    return player_link.get_attribute("href")
    # player_link.click()
    # print(driver.title)
            

def get_stats(url):
    r = requests.get(url, headers = {"User-Agent" : "Mozilla/5.0"})
    tables = pd.read_html(r.text, match = "Schedule/Results")
    stats_table_temp = tables[1]
    stats_df = pd.DataFrame(stats_table_temp.values[2:], columns = stats_table_temp.iloc[1])
    print(stats_df)

def create_player_profile(url):
    r = requests.get(url, headers = {"User-Agent" : "Mozilla/5.0"})
    print(url)
    team = driver.find_element(By.XPATH, "//legend/a[@target = 'ATHLETICS_URL']")
    print(team.text)



create_player_profile(get_player_URL("Jocelyn Alo"))

currentProfile = None
app.secret_key = "hi"

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

#setting up profiles
profiles = [{
    'username': 'user1',
    'password': 'user1'
}, {
    'username': 'user2',
    'password': 'user2'
}, {
    'username': 'user3',
    'password': 'user3'
}]

#home page
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/welcome")
@login_required
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        print(profiles)
        for user in profiles:
            print(user['username'] + " " + user['password'])
            if request.form['username'] == user['username']and request.form['password'] == user['password']:
                error = None
                session['logged_in'] = True
                flash('You were just logged in!')
                return redirect(url_for('welcome'))
            else:
                error = 'Incorrect username or password'

    return render_template('login.html', error = error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('home'))

app.run(debug = True)