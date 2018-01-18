from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import json


chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.mobile.de/')

select_box = driver.find_element_by_id("qsmakeBuy") 
options = [x for x in select_box.find_elements_by_tag_name("option")] #this part is cool, because it searches the elements contained inside of select_box and then adds them to the list options if they have the tag name "options"
data = {}
data['cars'] = []
models = []
for element in options:
    print(element.get_attribute("text"))
    make = element.get_attribute("text")
    element.click()
    time.sleep(1)
    model_select_box = driver.find_element_by_id("qsmodelBuy")
    model_options = [x for x in model_select_box.find_elements_by_tag_name("option")]
    for el in model_options:
        model = el.get_attribute("text")
        models.append(model)
    try:
        print(models)
    except:
        print("could not print")
    try:
        data['cars'].append([{"make": make}, {"model": models}])
    except:
        print("could not append")
    try:
        with open('cars.json', 'w') as outfile:  
            cars = json.dumps(data, sort_keys=True, indent=4)
            outfile.write(cars)
    except:
        print("could not write to file")
    models = []

#with open('cars.json', 'w') as outfile:  
#    cars = json.dumps(data, sort_keys=True, indent=4)
#    outfile.write(cars)

    

   

    
