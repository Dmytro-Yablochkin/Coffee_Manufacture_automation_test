from robot.libraries.BuiltIn import BuiltIn
from UserData import UserData

bi = BuiltIn()
sl = BuiltIn().get_library_instance("SeleniumLibrary")

# ----- Test requires user intervention ---- #


class Registration_Locators:
    costumer_icon = 'css = #site-navigation > div.right-block > div.topbar-link > div.account-block > ' \
                    'div.topbar-link-toggle '
    registration_dropdown = 'css = #site-navigation > div.right-block > div.topbar-link > div.topbar-link-wrapper'
    registration_link = 'css = #site-navigation > div.right-block > div.topbar-link >' \
                        ' div.topbar-link-wrapper > div > a:nth-child(2)'


# 1. Customer registration
class RegistrationForm:
    def fill_registration_form(self):
        sl.maximize_browser_window()
        bi.run_keyword('Click element', Registration_Locators.costumer_icon)
        bi.run_keyword('Wait until page contains element', Registration_Locators.registration_dropdown)
        # bi.run_keyword('Click link', Registration_Locators.registration_link)


    def empty_field_registration_form(self):
        sl.maximize_browser_window()
        bi.run_keyword('Click element', Registration_Locators.costumer_icon)
        bi.run_keyword('Wait until page contains element', Registration_Locators.registration_dropdown)
        # bi.run_keyword('Click link', Registration_Locators.registration_link)
