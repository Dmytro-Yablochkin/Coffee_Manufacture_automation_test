from robot.libraries.BuiltIn import BuiltIn
from UserData import UserData
from RegistrationForm import Registration_Locators

bi = BuiltIn()
sl = BuiltIn().get_library_instance("SeleniumLibrary")


class Authorization_locators:
    authorization_link = 'css = #site-navigation > div.right-block > div.topbar-link >' \
                         ' div.topbar-link-wrapper > div > a:nth-child(1)'
    email_field = 'css = input#username'
    password_field = 'css = input#password'
    remember_checkbox = 'css = input#rememberme'
    submit_btn = 'css = button.woocommerce-button.button.woocommerce-form-login__submit'

    logout_link = 'css = #site-navigation > div.right-block > div.topbar-link > div.topbar-link-wrapper > div > a'


class AuthorizationForm(Registration_Locators, UserData):
    def authorization_page(self):
        sl.maximize_browser_window()
        bi.run_keyword('Click element', Registration_Locators.costumer_icon)
        bi.run_keyword('Wait until page contains element', Registration_Locators.registration_dropdown)
        bi.run_keyword('Click link', Authorization_locators.authorization_link)

    # 3.Authorization
    def authorization(self):
        bi.run_keyword('authorization_page')
        bi.run_keyword('Input text', Authorization_locators.email_field, UserData.user_email)
        bi.run_keyword('Input text', Authorization_locators.password_field, UserData.user_password)
        bi.run_keyword('Click element', Authorization_locators.remember_checkbox)
        bi.run_keyword('Click button', Authorization_locators.submit_btn)

    def authorization_form_input(self):
        bi.run_keyword('authorization_page')
        bi.run_keyword('authorization')
        bi.run_keyword('Click element', Registration_Locators.costumer_icon)
        bi.run_keyword('Wait until element contains', Registration_Locators.registration_dropdown, 'Вихід')

    # 4.Authorization: With wrong email, Empty password field
    def authorization_bad_test1(self):
        bi.run_keyword('authorization_page')
        bi.run_keyword('Input text', Authorization_locators.email_field, UserData.bad_email)
        bi.run_keyword('Click element', Authorization_locators.remember_checkbox)
        bi.run_keyword('Click button', Authorization_locators.submit_btn)
        bi.run_keyword('Wait until page contains element', Authorization_locators.email_field)

    # 5. Authorization: With empty email field, Wrong password
    def authorization_bad_test2(self):
        bi.run_keyword('authorization_page')
        bi.run_keyword('Input text', Authorization_locators.password_field, UserData.bad_password)
        bi.run_keyword('Click element', Authorization_locators.remember_checkbox)
        bi.run_keyword('Click button', Authorization_locators.submit_btn)
        bi.run_keyword('Wait until page contains element', Authorization_locators.password_field)

    # 6. Logout
    def log_out(self):
        bi.run_keyword('authorization')
        bi.run_keyword('Click element', Registration_Locators.costumer_icon)
        bi.run_keyword('Wait until element contains', Registration_Locators.registration_dropdown, 'Вихід')
        bi.run_keyword('Click link', Authorization_locators.logout_link)
        bi.run_keyword('Wait until page contains element', Authorization_locators.email_field)


