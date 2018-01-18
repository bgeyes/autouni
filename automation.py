from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

class auto_bet:

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('https://www.unibet.ro/betting#filter/all/all/all/all/in-play')

    def __init__(self, amount):
        self.amount = amount

    def login(self, user, password):
        
        self.user = user
        self.password = password
        username = self.driver.find_element_by_name('username')
        passw = self.driver.find_element_by_name('password')
        username.send_keys(user)
        passw.send_keys(password)
        self.driver.find_element_by_class_name('primary_1s7tjyt-o_O-button_14j0avi-o_O-block_1ladoiw-o_O-headerButton_168fxbi-o_O-last_1uyqjoy-o_O-inlineButton_120drhm').click()

    def get_odds(self):

        odds = self.driver.find_elements_by_css_selector('button.KambiBC-mod-outcome')

        return odds

    def process_bets(self):
        count = 0
        print("getting odds")
        odds_list = self.get_odds()
        for odd in odds_list:
            self.check_balance()
            odd_element = str(odd.text)
            odds_sp = odd_element.split("\n")
            print(odds_sp)
            for el in odds_sp:
                try:
                    if float(el) < 1.27 and float(el) > 1.24:
                        print(el)
                        odds_list[count].click()
                        self.check_odd_adjustment()
                        self.get_bet_input_field()
                        time.sleep(1)
                        self.place_bet()
                        time.sleep(2)
                        self.close_bet()
                        time.sleep(2)
                except Exception as e:
                    print("not processed")

            count = count + 1


    def get_bet_input_field(self):
        try:
            input_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="KambiBC-outcome-items"]/li/article/section[8]/input[2]'))
            )
        except Exception as er:
            print(er)
        #not an integer
        print('input found')
        #inputing the betting amount
        input_field.send_keys(self.amount)


    def place_bet(self):
        try:
            place_bet = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'button.KambiBC-placebet-container__place'))
            )
        except Exception as er:
            print(er)
        print('button found')
        #time.sleep(1)
        place_bet.click()  


    def close_bet(self):
        try:
            close_b = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.KambiBC-close-receipt'))
            )
        except Exception as er:
            print(er)              
        close_b.click()
        print('bet closed')  


    def refresh_page(self):
        self.driver.refresh()


    def check_odd_adjustment(self):
        try:
            adjusted_odd = WebDriverWait(self.driver, 1).until(
                 EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.KambiBC-outcome-item__actions-dialogue'))
            )
            adjusted_odd.click()
            print('adjustment clicked')
        except Exception as er:
            print('adjsutment button not active')  

    def close_summary_screen(self):
        try:
            summary_button = WebDriverWait(self.driver, 1).until(
                 EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.primary_1s7tjyt-o_O-button_14j0avi'))
            )
            summary_button.click()
            print('summary closed')
        except Exception as er:
            print('summary not active')

    def check_balance(self):
        balance = self.driver.find_element_by_class_name('total-amount')
        print(balance.text)

        balancce_amount = balance.text
        balancce_amount.split(" ")

        if float(balancce_amount[0]) > 20:
            print("balance too low")
            time.sleep(1800)
            print("slept 30 minutes")
        else:
            print("balance bigger than 20 lei")
    
    def find_close_buttons(self):
        try:
            close_buttons = self.driver.find_elements_by_class_name('KambiBC-outcome-item__close-icon')
            #print('close buttons found, length of array ' + len(close_buttons))
            button_count = 0
            for button in close_buttons:
                close_buttons[button_count].click()
                print(button_count + ' button closed')
                #button_count += 1
            print('close buttons found, length of array ' + len(close_buttons))
                
        except Exception as ber:
            print("buttons not found")
        
        

if __name__ == '__main__':
    bet = auto_bet('1')
    bet.login('ionathanr@yahoo.co.uk', '')
    time.sleep(5)
    while True:

        print('\n\n#######  ' + str(datetime.now().time()) + '  #######\n\n')
        bet.find_close_buttons()
        bet.close_summary_screen()
        bet.process_bets()
        print('\n\n#######  ' + str(datetime.now().time()) + '  #######\n\n')
        time.sleep(120)
        bet.refresh_page()
        time.sleep(10)
    
