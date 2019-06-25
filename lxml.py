from lxml.html import fromstring, tostring

page=fromstring\
(
    '''
    <html>
    <body>
    hi
    <form name='test' method='post' action='/test'>
    Your name: <input type="text" name="user" value='nav'> <br>
    Your phone: <input type="password" name="password" value='secret'> <br>
    </form>
    </body>
    </html>
    '''
)

# print(page.forms[0].method)
# print(page.forms[0].action)
# print(page.forms[0].form_values())

inputs=page.forms[0].inputs

for input in inputs:
    if input.type=='text':
        username=input.name
    if input.type=='password':
         password=input.name