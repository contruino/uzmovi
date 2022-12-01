from flask import Flask
from flask_restful import Resource,Api
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
from bs4 import *

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self, search):
        sayt=f"https://www.uzmovi.com/search?q={search}"

        film=requests.get(sayt).text
        soup=BeautifulSoup(film, "lxml")
        kino=soup.find_all(class_="shortstory-in categ")

        options=webdriver.ChromeOptions()
        driver=webdriver.Chrome(executable_path="chromedriver.exe",options=options)

        for kn in kino:
            films=kn.find(class_="short-images-link").get("href")
            driver.get(films)
            info=driver.find_element(By.CLASS_NAME, "finfo").get_attribute("innerText")
            return info, films

api.add_resource(Home, "/<string:search>")

