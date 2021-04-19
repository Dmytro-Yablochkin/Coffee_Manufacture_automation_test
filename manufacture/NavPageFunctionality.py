from robot.libraries.BuiltIn import BuiltIn

bi = BuiltIn()
sl = BuiltIn().get_library_instance("SeleniumLibrary")


class NavigationLocators:
    page_footer = 'css = #colophon > div.footer-bottom > div > div'
    page_header = 'css = #masthead > div.topbar-outer'

    scroll_btn = 'css = #to_top'

    right_btn = 'css = #rev_slider_1_1 > div.tp-rightarrow.tparrows.persephone'
    left_btn = 'css = #rev_slider_1_1 > div.tp-leftarrow.tparrows.persephone'

    photo_slider = 'css = #rev_slider_1_1'
    photo_right = 'css = div#rev_slider_1_1[data-slideactive="rs-15"]'
    photo_left = 'css = div#rev_slider_1_1[data-slideactive="rs-16"]'

    nav_panel_places = 'css = #menu-top-1 > li.menu-item.menu-item-type-post_type.menu-item-object-page.menu-item' \
                       '-8124 > a '
    nav_panel_store = 'css = #menu-top-1 > li.menu-item.menu-item-type-custom' \
                      '.menu-item-object-custom.menu-item-has-children.menu-item-8455'
    nav_panel_droplist = 'css = #menu-top-1 > li.menu-item.menu-item-type-custom.menu-item-object-custom' \
                         '.menu-item-has-children.menu-item-8455 > div > ul'
    nav_droplist_weight = 'css = #menu-top-1 > li.menu-item.menu-item-type-custom.menu-item-object-custom.menu-item' \
                          '-has-children.menu-item-8455 > div > ul > ' \
                          'li.menu-item.menu-item-type-custom.menu-item-object-custom.menu-item-8681 > a '
    nav_droplist_mulled = 'css = #menu-top-1 > li.menu-item.menu-item-type-custom.menu-item-object-custom.menu-item-has' \
                          '-children.menu-item-8455 > div > ul > ' \
                          'li.menu-item.menu-item-type-custom.menu-item-object-custom.menu-item-8653 > a '
    nav_droplist_packaged = 'css = #menu-top-1 > li.menu-item.menu-item-type-custom.menu-item-object-custom.current' \
                            '-menu' \
                            '-ancestor.current-menu-parent.menu-item-has-children.menu-item-8455 > div > ul > ' \
                            'li.menu-item.menu-item-type-custom.menu-item-object-custom.menu-item-7604 > a '
    nav_droplist_souvenirs = 'css = #menu-top-1 > li.menu-item.menu-item-type-custom.menu-item-object-custom.menu' \
                             '-item-has-children.menu-item-8455 > div > ul > ' \
                             'li.menu-item.menu-item-type-custom.menu-item-object-custom.menu-item-7598 > a '


class NavPageFunctionality:
    # 7. Auto-scroll button
    def auto_scroll_btn(self):
        sl.maximize_browser_window()
        bi.run_keyword('Scroll element into view', NavigationLocators.page_footer)
        bi.run_keyword('Wait until page contains element', NavigationLocators.scroll_btn)
        bi.run_keyword('Click element', NavigationLocators.scroll_btn)
        bi.run_keyword('Wait until element is visible', NavigationLocators.page_header)

    # 8. Photo scrolling button right/left
    def click_right_and_left_btns(self):
        sl.maximize_browser_window()
        bi.run_keyword('Mouse over', NavigationLocators.photo_slider)
        bi.run_keyword('Wait until element is visible', NavigationLocators.right_btn)
        bi.run_keyword('Click element', NavigationLocators.right_btn)
        bi.run_keyword('Wait until page contains element', NavigationLocators.photo_right)
        bi.run_keyword('Click element', NavigationLocators.left_btn)
        bi.run_keyword('Wait until page contains element', NavigationLocators.photo_left)

    # 9. Navigation panel droplist
    def hover_on_nav_item(self):
        sl.maximize_browser_window()
        bi.run_keyword('Mouse over', NavigationLocators.nav_panel_store)
        bi.run_keyword('Wait until element is visible', NavigationLocators.nav_panel_droplist)
