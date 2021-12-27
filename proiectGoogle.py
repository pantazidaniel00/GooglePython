import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.emag.ro/#opensearch')
get_element = browser.find_element(By.ID, 'searchboxTrigger')
get_element.send_keys('Telefoane')
get_element.submit()
product = browser.find_elements(By.CLASS_NAME, 'card-item')

listOfProducts = []
dictionary = {}

regex3 = r"Telefon(.*)"

# Prelucrarea rezultatelor
for i in range(len(product)-6):  # -6 din lungime - apareau inca 6 clase goale, fara detalii, indiferent de cautare
    string_to_write = '{number}.'.format(number=i+1) + product[i].text
    listOfProducts.append(string_to_write)

    # print(listOfProducts[i].split())
    # print(re.search(regex3, listOfProducts[i]).group())

    # creez dictionarul cu telefonul si pretul fiecaruia, elimin punctele din preturi
    if (listOfProducts[i].split()[-3])[0].isnumeric():
        dictionary[re.search(regex3, listOfProducts[i]).group()] = (listOfProducts[i].split()[-3].replace('.', ''))[:-2]
    elif (listOfProducts[i].split()[-4])[0].isnumeric():
        dictionary[re.search(regex3, listOfProducts[i]).group()] = (listOfProducts[i].split()[-4].replace('.', ''))[:-2]
    else:
        dictionary[re.search(regex3, listOfProducts[i]).group()] = (listOfProducts[i].split()[-5].replace('.', ''))[:-2]
print(dictionary)

# Filtrare de catre utilizator
question1 = input("Doriti un brand anume? Da/Nu: ")
if question1 == 'Da' or question1 == 'da':
    brand = input("Brand-ul dorit: ")
else:
    brand = None

question2 = input("Doriti sa setati un prag maxim de pret? Da/Nu: ")
if question2 == 'Da' or question2 == 'da':
    max_price = int(input("Pret maxim: "))
else:
    max_price = None

if brand is not None:
    if max_price is not None:
        for i in dictionary:
            if brand in i:
                if max_price >= int(dictionary[i]):
                    print(i + ', ' + dictionary[i] + ' Lei')
    else:
        for i in dictionary:
            if brand in i:
                print(i + ', ' + dictionary[i] + ' Lei')
else:
    for i in dictionary:
        print(i + ', ' + dictionary[i] + ' Lei')

time.sleep(5)
