from selene.support.shared import browser

class LoginPage:
    def login_user(self):
        browser.open('/login')
        browser.element('#LOGINUSERNAME').type('admin@pryaniky.com')
        browser.element('#LOGINPASSWORD').type('9qgc0s6n')
        browser.element('#LOGINENTERBUTTON').click()
