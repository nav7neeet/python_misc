from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def extract_login_details(url):
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(url)

    forms = browser.find_elements_by_xpath('//form')
    print(f'number of forms is {len(forms)}')

    for i in range(len(forms)):
        inputs = browser.find_elements_by_xpath(f'//form[{i+1}]/input')
        print(f'number of input elements in form{i} is {len(inputs)}')

#     test = browser.find_elements_by_xpath('//form[2]/input')
#     print(len(test))

extract_login_details('http://localhost:8081/PrivEscalation/')
