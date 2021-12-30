import random
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options, executable_path='/utilities/geckodriver')
# Add '?tab=all_releases' to the end of the link to filter only for the all the releases
# link = link + '?tab=all_releases'
browser.get('https://bandcamp.com/tag/electronic?tab=all_releases')
first_artist_link = browser.find_element(By.CSS_SELECTOR, 'div.dig-deeper-item:nth-child(1) > div:nth-child(2) > a:nth-child(1)')
first_artist_band_name = browser.find_element(By.CSS_SELECTOR, 'div.dig-deeper-item:nth-child(1) > div:nth-child(2) > a:nth-child(1) > div:nth-child(2) > span:nth-child(1)')
first_artist_album_name = browser.find_element(By.CSS_SELECTOR, 'div.dig-deeper-item:nth-child(1) > div:nth-child(2) > a:nth-child(1) > div:nth-child(1)')
print('\n\nFIRST ARTIST: ')
print('first_artist_link: %s' %(first_artist_link.get_attribute('href')))
print('first_artist_band_name: %s' %(first_artist_band_name.text))
print('first_artist_album_name: %s' %(first_artist_album_name.text))
second_artist_link = browser.find_element(By.CSS_SELECTOR, 'div.dig-deeper-item:nth-child(2) > div:nth-child(2) > a:nth-child(1)')
second_artist_band_name = browser.find_element(By.CSS_SELECTOR, 'div.dig-deeper-item:nth-child(2) > div:nth-child(2) > a:nth-child(1) > div:nth-child(2) > span:nth-child(1)')
second_artist_album_name = browser.find_element(By.CSS_SELECTOR, 'div.dig-deeper-item:nth-child(2) > div:nth-child(2) > a:nth-child(1) > div:nth-child(1)')
print('\n\nSECOND ARTIST: ')
print('second_artist_link: %s' %(second_artist_link.get_attribute('href')))
print('second_artist_band_name: %s' %(second_artist_band_name.text))
print('second_artist_album_name: %s' %(second_artist_album_name.text))
third_artist_link = browser.find_element(By.CSS_SELECTOR, 'div.dig-deeper-item:nth-child(3) > div:nth-child(2) > a:nth-child(1)')
third_artist_band_name = browser.find_element(By.CSS_SELECTOR, 'div.dig-deeper-item:nth-child(3) > div:nth-child(2) > a:nth-child(1) > div:nth-child(2) > span:nth-child(1)')
third_artist_album_name = browser.find_element(By.CSS_SELECTOR, 'div.dig-deeper-item:nth-child(3) > div:nth-child(2) > a:nth-child(1) > div:nth-child(1)')
print('\n\nTHIRD ARTIST: ')
print('third_artist_link: %s' %(third_artist_link.get_attribute('href')))
print('third_artist_band_name: %s' %(third_artist_band_name.text))
print('third_artist_album_name: %s' %(third_artist_album_name.text))
