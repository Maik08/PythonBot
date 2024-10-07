from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Chrome-Optionen erstellen
chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:\\Users\\Maik\\AppData\\Local\\Google\\Chrome\\User Data")  # Pfad zum Benutzerprofil
chrome_options.add_argument("profile-directory=Default")  # Profilname (kann je nach Bedarf angepasst werden)


# Webdriver initialisieren
driver = webdriver.Chrome(options=chrome_options)
Futbin = 'https://www.futbin.com/'

def SnipingFrage():
    Sniping_Coins = input("FOR HOW MUCH YOU WANNA SNIPE?")
    Selling_Coins = input("FOR HOW MUCH YOU WANNA SELL?")
    print(f"is this correct?: {Sniping_Coins}")
    print(f"is this correct?: {Selling_Coins}")
    print("---------------------")
    Continue = input("Continue?...Y/GoBack...")
    
    if Continue == "Y":
        Sniping()
        
    if Continue == "GoBack":
        SnipingFrage()
        
        
def Sniping():
    print(f"cool")
    
        


try:
    time.sleep(3)
    print("----------------------")
    spieler_name = input("🇵‌🇱‌🇦‌🇾‌🇪‌🇷‌... ")
    print("----------------------")
    

    # Öffne die Webseite
    driver.get(Futbin)
    driver.implicitly_wait(2)

    search_input = driver.find_element(By.XPATH, '//*[@id="playerSearch"]/div/input')
    

    search_input.click()
    

    # Buchstaben einzeln eingeben
    for buchstabe in spieler_name:
        search_input.send_keys(buchstabe)
        time.sleep(0.03)

    time.sleep(1)  # Warte etwas, um sicherzustellen, dass der Text eingegeben wurde
    search_input.send_keys(Keys.ENTER)  # Drücke Enter
     # Warte auf das Laden der Ergebnisse

    # Suche nach dem Preis
    parent_element = driver.find_element(By.CSS_SELECTOR, '.price-box.player-price-not-pc.price-box-original-player')
    column_element = parent_element.find_element(By.CSS_SELECTOR, '.column')
    price_element = column_element.find_element(By.CSS_SELECTOR, '.price.inline-with-icon.lowest-price-1')
    

    # Preis ausgeben
    preis = price_element.text
   
    print(f"𝖈𝖚𝖗𝖗𝖊𝖓𝖙 𝖕𝖗𝖎𝖈𝖊: {preis}")
    print(f"----------------------")
    
    
    Snipingactive = input("𝖆𝖈𝖙𝖎𝖛𝖆𝖙𝖊 𝖘𝖓𝖎𝖕𝖎𝖓𝖌...Y/N")
    print(f"----------------------")
    
    if Snipingactive == "Y":
        SnipingFrage()
        
    if Snipingactive == "N":
        driver.quit()
        
        

except ZeroDivisionError:
    driver.quit()

finally:
    driver.quit()
