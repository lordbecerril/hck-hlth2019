'''
PURPOSE:
    The purpose of this script is to open a specific youtube and take screenshots of the screen.

AUTHORS:
    Eric Becerril-Blas - Github: https://github.com/lordbecerril
    Zoyla Orellana - Github: https://github.com/ZoylaO

'''
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import threading
import time

# Using Chrome to access web
driver = webdriver.Chrome()

# Open the specific youtube video we are interested in
driver.get("https://www.youtube.com/watch?v=ac4DQqij3Bg")

#Let the page load up
time.sleep(5)

MakeFullScreen = driver.find_element_by_xpath("//*[@id=\"movie_player\"]/div[20]/div[2]/div[2]/button[9]")
MakeFullScreen.send_keys("\n")

#let the page load up
time.sleep(60)

killPopUp = driver.find_element_by_xpath("/html/body/ytd-app/ytd-popup-container/paper-dialog/ytd-mealbar-promo-renderer/div/div[2]/ytd-button-renderer[1]/a/paper-button/yt-formatted-string")
try:
    killPopUp.send_keys("\n")
except:
    print("dang")

count = 0
while True:
    driver.save_screenshot("./raw/screenshot"+str(count)+".png")
    time.sleep(1)
    count = count + 1



'''
# Youtube Search
youtube_search = driver.find_element_by_xpath("//*[@id=\"search\"]")

#Let the page load up
time.sleep(5)

youtube_search.send_keys("Epileptic Seizure") #Searches for
'''
