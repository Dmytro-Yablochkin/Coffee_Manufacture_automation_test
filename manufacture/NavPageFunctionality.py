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

    top_sells_block = 'css = #post-212 > div > div.vc_row.wpb_row.vc_row-fluid.producttab.vc_custom_1590763826914' \
                      '.vc_row-has-fill > div > div > div '

    top_sells_item = 'css = li.post-2491.product.type-product.status-publish.has-post-thumbnail.product_cat-packed' \
                     '-coffee.product_tag-200-.product_brand-113.instock.sale.featured.shipping-taxable.purchasable' \
                     '.product-type-simple '

    top_sells_rb = 'css = div > ul > div.owl-controls.clickable > div > div.owl-next'
    top_sells_lb = 'css = div > ul > div.owl-controls.clickable > div > div.owl-prev'

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
        
        # 20. Item scroll button Left/Right
    def top_sells_block_btns(self):
        sl.maximize_browser_window()
        bi.run_keyword('Scroll element into view', NavigationLocators.top_sells_block)
        bi.run_keyword('Mouse over', NavigationLocators.top_sells_item)
        bi.run_keyword('Wait until element is visible', NavigationLocators.top_sells_rb)
        bi.run_keyword('Click element', NavigationLocators.top_sells_rb)
        bi.run_keyword('Wait until element is visible', NavigationLocators.top_sells_lb)
        bi.run_keyword('Click element', NavigationLocators.top_sells_lb)
        bi.run_keyword('Wait until page contains element', NavigationLocators.top_sells_item)
