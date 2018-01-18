from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get('https://www.unibet.ro/betting#filter/all/all/all/all/in-play')

user = 'ionathanr@yahoo.co.uk'
passw = ''

username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')

username.send_keys(user)
password.send_keys(passw)

driver.find_element_by_class_name('primary_1s7tjyt-o_O-button_14j0avi-o_O-block_1ladoiw-o_O-headerButton_168fxbi-o_O-last_1uyqjoy-o_O-inlineButton_120drhm').click()

time.sleep(10)

odds = driver.find_elements_by_css_selector('button.KambiBC-mod-outcome')

amount = '1'
count = 0



for odd in odds:
    odd_element = str(odd.text)
    odds_sp = odd_element.split("\n")
    print(odds_sp)
    for el in odds_sp:
        try:
            if float(el) < 1.11 and float(el) > 1.01:
                print(el)
                odds[count].click()
                try:
                    close_buttons = driver.find_elements_by_class_name('KambiBC-outcome-item__close-icon')
                    print('close buttons found')
                    button_count = 0
                    for button in close_buttons:
                        close_buttons[button_count].click()
                        button_count += 1
                except Exception as ber:
                    print("buttons not found")
                time.sleep(2)
                #finding the input field
                #input_field = driver.find_element_by_xpath('//*[@id="KambiBC-outcome-items"]/li/article/section[8]/input[2]')
            

                try:
                    adjusted_odd = WebDriverWait(driver, 1).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.KambiBC-outcome-item__actions-dialogue'))
                    )
                    adjusted_odd.click()
                    print('adjustment clicked')
                except Exception as er:
                    print(er)              
                
                    
                try:
                    input_field = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="KambiBC-outcome-items"]/li/article/section[8]/input[2]'))
                    )
                except Exception as er:
                    print(er)
                #not an integer
                print('input found')
                #inputing the betting amount
                input_field.send_keys(amount)
                #searching for the placing bet button
                #place_bet = driver.find_element_by_css_selector('button.KambiBC-placebet-container__place')
                try:
                    place_bet = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'button.KambiBC-placebet-container__place'))
                    )
                except Exception as er:
                    print(er)
                print('button found')
                #time.sleep(1)
                place_bet.click()
                time.sleep(2)
                #searching for the close bet after placing it button
                #close_b = driver.find_element_by_css_selector('button.KambiBC-close-receipt')  
                try:
                    close_b = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.KambiBC-close-receipt'))
                    )
                except Exception as er:
                    print(er)              
                close_b.click()
                print('bet closed')
                time.sleep(2)
        except Exception as e:
            #not an integer
            print(e)
    
    count = count + 1
    



