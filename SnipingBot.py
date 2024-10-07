from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()  
Spieler = 'https://www.futbin.com/25/player/32868/patricia-guijarro-gutierrez'


try:
    
    # Öffne die Webseite
    driver.get(Spieler)

    #suche nach preis
    parent_element = driver.find_element(By.CSS_SELECTOR, '.price-box.player-price-not-pc.price-box-original-player')
    column_element = parent_element.find_element(By.CSS_SELECTOR, '.column')
    price_element = column_element.find_element(By.CSS_SELECTOR, '.price.inline-with-icon.lowest-price-1')


    #preis ausgeben
    preis = price_element.text
    print (f"----------------------")
    print (f"𝖈𝖚𝖗𝖗𝖊𝖓𝖙 𝖕𝖗𝖎𝖈𝖊: {preis}")
    print (f"----------------------")

    driver.quit()


except ZeroDivisionError:
    print("Geht nicht lol")
    driver.quit()
