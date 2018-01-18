try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()



driver.findElements(By.tag(‘button’))[4]

//a[starts-with(@id, "yui_3_5_0_1")]

driver.find_elements(By.XPATH, '//button')

for option in options:
    options_reference.append(option.text)

for option in options_reference:
    option_element = driver.find_element_by_xpath(
            "//*[contains(text(), '" + option + "')]")
    option_element.click()






KambiBC-outcome-item__stake__input KambiBC-stake-input KambiBC-js-otc__stake-input

KambiBC-placebet-container__place

KambiBC-close-receipt

driver.get("http://somedomain/url_that_delays_loading")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()




KambiBC-outcome-item__actions-dialogue