from robot.libraries.BuiltIn import BuiltIn
from NavPageFunctionality import NavigationLocators

bi = BuiltIn()
sl = BuiltIn().get_library_instance("SeleniumLibrary")

class Other_locators:
    places_page = 'css = #main > div > div.page-title.header > div'

class OtherSiteInfo(NavigationLocators):
    # 17. Other site information
    def redirect_to_places_page(self):
        sl.maximize_browser_window()
        bi.run_keyword('Click link', NavigationLocators.nav_panel_places)
        bi.run_keyword('Wait until page contains element', Other_locators.places_page)
