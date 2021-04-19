from robot.libraries.BuiltIn import BuiltIn
from NavPageFunctionality import NavigationLocators
from ProductItemLocators import ProductItemLocators

bi = BuiltIn()
sl = BuiltIn().get_library_instance("SeleniumLibrary")


class CartLocators:
    add_to_cart_btn = 'css = li.post-8298.product.type-product.status-publish.has-post-thumbnail.product_cat' \
                      '-pregrinded_coffee.product_tag-200-.instock.sale.featured.shipping-taxable.purchasable.product' \
                      '-type-simple > div > div > div.product-detail-wrapper > div.product-block-hover > div > a '
    souvenir_add_to_cart_btn = 'css = #content > ul > li.post-7685.product.type-product.status-publish.has-post' \
                               '-thumbnail.product_cat-coffee-cosmetics.product_cat-souvenirs.product_tag-5-.first' \
                               '.instock.shipping-taxable.purchasable.product-type-simple > div > div > ' \
                               'div.product-detail-wrapper > div.product-block-hover > div > a '

    options_btn1 = 'css = li.status-publish.has-post-thumbnail.product_cat-arabika.product_cat-weighed-out-coffee' \
                   '.product_tag-100-.first.instock.shipping-taxable.purchasable.product-type-variable > div > div > ' \
                   'div.product-detail-wrapper > div.product-block-hover > div > a '

    options_droplist = 'css = td.value select'
    options_droplist_item5 = 'css = option:nth-child(5)'
    options_droplist_item3 = 'css = option:nth-child(3)'
    options_droplist_item8 = 'css = option:nth-child(8)'
    options_droplist_keychain = 'css = option:nth-child(3)'

    opt_add_to_cart_btn = 'css = .variations_button.woocommerce-variation-add-to-cart-enabled > button'

    add_agree_msg = 'css = #content > div.woocommerce-notices-wrapper > div'
    cart_redirect_btn = 'css = #content > div.woocommerce-notices-wrapper > div > a'
    quantity_input = 'css = div.woocommerce-variation-add-to-cart div > input'
    remove_sign = 'css = td.removepro > a'
    remove_alert = '“Арабіка Бразилія Бурбон” видалено. '


class CartFunctionality(NavigationLocators, ProductItemLocators):
    def del_item(self):
        bi.run_keyword('Click element', CartLocators.cart_redirect_btn)
        bi.run_keyword('Click link', CartLocators.remove_sign)

    # 10. Add item to cart
    def add_item(self):
        sl.maximize_browser_window()
        bi.run_keyword('Mouse over', NavigationLocators.nav_panel_store)
        bi.run_keyword('Wait until element is visible', NavigationLocators.nav_panel_droplist)
        bi.run_keyword('Click link', NavigationLocators.nav_droplist_mulled)
        bi.run_keyword('Mouse over', ProductItemLocators.kaianza)
        bi.run_keyword('Wait until element is visible', CartLocators.add_to_cart_btn)
        bi.run_keyword('Click link', CartLocators.add_to_cart_btn)
        bi.run_keyword('Wait until page contains element', CartLocators.add_agree_msg)
        bi.run_keyword('del_item')

    # 11. Delete item from the cart
    def delete_item(self):
        sl.maximize_browser_window()
        bi.run_keyword('Mouse over', NavigationLocators.nav_panel_store)
        bi.run_keyword('Wait until element is visible', NavigationLocators.nav_panel_droplist)
        bi.run_keyword('Click link', NavigationLocators.nav_droplist_weight)
        bi.run_keyword('Mouse over', ProductItemLocators.bourbon)
        bi.run_keyword('Click link', CartLocators.options_btn1)
        bi.run_keyword('Click element', CartLocators.options_droplist)
        bi.run_keyword('Click element', CartLocators.options_droplist_item5)
        bi.run_keyword('Clear element text', CartLocators.quantity_input)
        bi.run_keyword('Input text', CartLocators.quantity_input, '4')
        bi.run_keyword('Click element', CartLocators.opt_add_to_cart_btn)
        bi.run_keyword('del_item')
        bi.run_keyword('Wait until page contains', CartLocators.remove_alert)

    # 20. Saving shopping cart information functionality
    def create_and_refresh(self):
        sl.maximize_browser_window()
        bi.run_keyword('OrderCreation.santos_making_order')
        bi.run_keyword('OrderCreation.order_user_data_input')
        sl.reload_page()
        bi.run_keyword('Wait until page contains element', CartLocators.remove_sign)
