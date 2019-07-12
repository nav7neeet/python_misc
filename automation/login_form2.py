from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from test import urls

def extract_login_details(url):
    user_var=''
    pass_var=''
    type=['text', 'email', 'username']
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(url)

    forms = browser.find_elements_by_xpath('//form')
    print(f'forms - {len(forms)}')
    
    for i in range(len(forms)):
        inputs = browser.find_elements_by_xpath(f'//form[{i+1}]//*/input | //form[{i+1}]/input')
        print(f'input tags in form{i+1} is {len(inputs)}')
        for input_tag in inputs:
            if any( word in input_tag.get_attribute('type') for word in type):
                user_var=input_tag.get_attribute('name')
            if input_tag.get_attribute('type')=='password':
                pass_var=input_tag.get_attribute('name')
        print(url, ' - ' , user_var, pass_var)
        print()
        
    browser.close()

for url in urls:
    extract_login_details(url)

# extract_login_details('http://localhost:8081/PrivEscalation/test2.jsp')
# extract_login_details('https://www.facebook.com/')