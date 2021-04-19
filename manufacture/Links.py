from robot.libraries.BuiltIn import BuiltIn
from NavPageFunctionality import NavigationLocators

bi = BuiltIn()
sl = BuiltIn().get_library_instance("SeleniumLibrary")

class Link_Locators:
    facebook_link = 'css = #followmewidget-4 > div > ul > li > a.facebook.icon'
    facebook_title = 'Львівська мануфактура кави - Главная | Facebook'

    instagram_link = 'css = #followmewidget-4 > div > ul > li > a.instagram.icon'
    instagram_title = 'Lviv Coffee Manufacture (@manufacture.coffee) • Фото и видео в Instagram'

class Links(NavigationLocators):
    def click_facebook_link(self):
        sl.maximize_browser_window()
        bi.run_keyword('Scroll element into view', NavigationLocators.page_footer)
        bi.run_keyword('Click link', Link_Locators.facebook_link)
        bi.run_keyword('Title should be', Link_Locators.facebook_title)

    def click_instagram_link(self):
        sl.maximize_browser_window()
        bi.run_keyword('Scroll element into view', NavigationLocators.page_footer)
        bi.run_keyword('Click link', Link_Locators.instagram_link)
        bi.run_keyword('Title should be', Link_Locators.instagram_title)