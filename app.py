from asyncio.windows_events import NULL
from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash
from functools import wraps
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import pandas as pd
import requests

#setting up Flask
app = Flask(__name__)

#setting up web scraping
# option = webdriver.ChromeOptions()
# option.add_argument('--headless')

# driver = webdriver.Chrome(service = Service("C:/Users/lelaj/Downloads/chromedriver_win32/chromedriver"), options = option)

#web scraping
def getTable(url):
    html_content = requests.get(url, headers = {'User-Agent': 'Chrome'}).text
    soup = BeautifulSoup(html_content, "lxml")

    table_list = "Schedule/Results".find_parent("div", class = "game_breakdown_div")
    print(table_list)


currentProfile = NULL
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