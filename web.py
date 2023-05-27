import os
os.system('sudo apt update')
os.system('sudo apt install python3 python3-dev python3-venv screen -y')
os.system('wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')
os.system('sudo -s dpkg -i google-chrome-stable_current_amd64.deb')
os.system('sudo apt-get -fy install')
os.system('pip3 install chromedriver-binary==110.0.5481.77')
os.system('pip install selenium')
from selenium import webdriver
import time
from time import sleep
myoptions = webdriver.ChromeOptions()
myoptions.add_argument("--headless")
myoptions.add_argument("--disable-gpu")
myoptions.add_argument("window-size=1024,768")
myoptions.add_argument("--no-sandbox")
driver = webdriver.Chrome('chromedriver',chrome_options=myoptions)
driver.get("https://google.com")
sleep(43500)
