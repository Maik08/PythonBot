from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import keyboard
import sys



# Chrome-Optionen erstellen
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:\\Users\\Maik\\AppData\\Local\\Google\\Chrome\\User Data")  # Pfad zum Benutzerprofil
chrome_options.add_argument("profile-directory=Default")  # Profilname (kann je nach Bedarf angepasst werden)

Futbin = 'https://www.futbin.com/'

# Webdriver als globale Variable initialisieren
driver = None

keyboard.add_hotkey('ctrl+c', lambda: sys.exit())
keyboard.wait



def main():
    print(f"----------------------")
    print("For Notes press ---'N'---   ")
    print(f"----------------------")
    print("made by Maik M.")
    print(f"----------------------")
    print(f"---Your Chrome Browser will open automatically. Be sure it is CLOSED BEFORE---")
    print(f"----------------------")
    print(f"----------------------")
    Start()
        



def Start():
    while True:
        print("Continue? press SPACE.BAR: ")
        print(f"----------------------")
        keyboard.add_hotkey('space', OpenFutbin)
        
        keyboard.add_hotkey('N', lambda: print("if your browser crashes check futbin.com manually and click the anti-bot box."))
        
        keyboard.wait('space')
        

def OpenFutbin():
    global driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(Futbin)
    driver.implicitly_wait(2)
    SpielerEingabe()


def SpielerEingabe():
    print("----------------------")
    spieler_name = input("🇵‌🇱‌🇦‌🇾‌🇪‌🇷‌... ")
    print("----------------------")
    
    try:
        search_input = driver.find_element(By.XPATH, '//*[@id="playerSearch"]/div/input')
        search_input.click()
    
        for buchstabe in spieler_name:
            search_input.send_keys(buchstabe)
            time.sleep(0.03)
    
        time.sleep(1)
        search_input.send_keys(Keys.ENTER)
         
        Preis()
    except Exception as e:
        print(f"Error while searching player: {e}")
        driver.quit()


def Preis():
    try:
        parent_element = driver.find_element(By.CSS_SELECTOR, '.price-box.player-price-not-pc.price-box-original-player')
        column_element = parent_element.find_element(By.CSS_SELECTOR, '.column')
        price_element = column_element.find_element(By.CSS_SELECTOR, '.price.inline-with-icon.lowest-price-1')

        preis = price_element.text
        print(f"𝖈𝖚𝖗𝖗𝖊𝖓𝖙 𝖕𝖗𝖎𝖈𝖊: {preis}")
        print(f"----------------------")

        Snipingactive = input("𝖆𝖈𝖙𝖎𝖛𝖆𝖙𝖊 𝖘𝖓𝖎𝖕𝖎𝖓𝖌...Y/N")
        print(f"----------------------")

        if Snipingactive == "Y":
            SnipingFrage()
        elif Snipingactive == "N":
            driver.quit()
    except Exception as e:
        print(f"Error while fetching price: {e}")
        driver.quit()


def SnipingFrage():
    while True:
        Sniping_Coins = input("FOR HOW MUCH YOU WANNA SNIPE? ")
        Selling_Coins = input("FOR HOW MUCH YOU WANNA SELL? ")
        print(f"is this correct? --Sniping--    {Sniping_Coins}")
        print(f"is this correct? --Selling--    {Selling_Coins}")
        print("---------------------")
        Continue = input("Continue?...Y/GoBack...") 

        if Continue == "Y":
            Sniping(Sniping_Coins, Selling_Coins) 
            break
        elif Continue == "GoBack":
            continue


def Sniping(snipe_price, sell_price):
    print(f"Sniping for {snipe_price} coins and selling for {sell_price} coins.")
    # Hier kommt die Logik zum Sniping rein
    print("Sniping started...")


if __name__ == "__main__":
    main()