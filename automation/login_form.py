from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from test import urls
from strings import User_Xpath, Pass_Xpath, Submit_Xpath, Not_Found, Any_Form, \
    Not_Displayed, Login_Form, Not_Login_Form


def extract_login_details(url):
    user_var = ''
    pass_var = ''
    type = ['text', 'email', 'username']
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options = options)
    browser.get(url)

    forms = browser.find_elements_by_xpath('//form')
    print(f'{url}: forms - {len(forms)}')
            
    if len(forms):            
        for i, form in enumerate(forms):
            if form.is_displayed():
                user_field = form.find_elements_by_xpath(User_Xpath)
                pass_field = form.find_elements_by_xpath(Pass_Xpath)
                submit_button = form.find_elements_by_xpath(Submit_Xpath)
                
                if (len(user_field) == 1 and len(submit_button) == 1) and len(pass_field) == 1:
                    for x in pass_field:
                        if x.is_displayed():
                            var = Login_Form
                        else:
                            var = Any_Form
                else:
                    var = Not_Login_Form
            else:
                var = Not_Displayed
            print(f'form{i+1} ' + var)
        print()
    else:
        print(Not_Found)
    browser.close()
    
# extract_login_details('http://localhost:8081/PrivEscalation/test2.jsp')
# extract_login_details('https://login.perfectmind.com/socialsite/memberregistration/membersignin')
# extract_login_details('https://www.facebook.com/')


for url in urls:
    extract_login_details(url)
