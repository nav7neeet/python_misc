User_Xpath = "./descendant::input[@type='text' or @type='email']"
Pass_Xpath = "./descendant::input[@type='password']" 
Submit_Xpath = "./descendant::input[@type='button' or @type='submit'] | ./descendant::button"

Not_Found = 'login form not found on the page'
Not_Displayed = 'is not displayed on the page'

Login_Form = '*login form*'
Not_Login_Form = 'not a login form'
Any_Form = 'can be a 2-step login form or password reset form or search form'
