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
            
    for form in forms:
        print(len(form.find_elements_by_xpath('./descendant::input')))           
            
#     for i in range(len(forms)):
# #         inputs = browser.find_elements_by_xpath(f'//form[{i+1}]//*/input | //form[{i+1}]/input')
#         inputs=forms[i].find_elements_by_xpath(f'//form[{i+1}]//*/input | //form[{i+1}]/input')
#         print(f'input tags in form{i+1} is {len(inputs)}')
#     browser.close()

extract_login_details('http://localhost:8081/PrivEscalation/test2.jsp')

# extract_login_details('https://login.perfectmind.com/socialsite/memberregistration/membersignin')
# extract_login_details('https://www.facebook.com/')