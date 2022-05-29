from flask import Flask, render_template, request, jsonify, redirect, url_for
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import pandas as pd
import requests

#setting up Flask
app = Flask(__name__)

#setting up web scraping
option = webdriver.ChromeOptions()
option.add_argument('--headless')

driver = webdriver.Chrome(service = Service("C:/Users/lelaj/Downloads/chromedriver_win32/chromedriver"), options = option)

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

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        print(profiles)
        for user in profiles:
            print(user['username'] + " " + user['password'])
            if request.form['username'] == user['username']and request.form['password'] == user['password']:
                return redirect(url_for('home'))
                error = none
            else:
                error = 'Incorrect username or password'

    return render_template('login.html', error = error)

app.run(debug = True)