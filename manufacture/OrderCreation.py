from robot.libraries.BuiltIn import BuiltIn
from NavPageFunctionality import NavigationLocators
from ProductItemLocators import ProductItemLocators
from CartFunctionality import CartLocators
from UserData import UserData

bi = BuiltIn()
sl = BuiltIn().get_library_instance("SeleniumLibrary")


class Order_Locators:
    options_btn_santos = 'css = #content > ul > li.post-7645.product.type-product.status-publish.has-post-thumbnail' \
                         '.product_cat-arabika.product_cat-weighed-out-coffee.product_tag-100-.instock.shipping-taxable' \
                         '.purchasable.product-type-variable > div > div > div.product-detail-wrapper > ' \
                         'div.product-block-hover > div > a '
    option_btn_burundi = 'css = #content > ul > li.post-8077.product.type-product.status-publish.has-post-thumbnail' \
                         '.product_cat-arabika.product_cat-weighed-out-coffee.product_tag-100-.last.instock.shipping' \
                         '-taxable.purchasable.product-type-variable > div > div > div.product-detail-wrapper > ' \
                         'div.product-block-hover > div > a '
    option_btn_keychain = 'css = #content > ul > li.post-7714.product.type-product.status-publish.has-post-thumbnail' \
                          '.product_cat-magnets.product_cat-souvenirs.instock.shipping-taxable.purchasable.product' \
                          '-type-variable > div > div > div.product-detail-wrapper > div.product-block-hover > div > a '

    name_field = 'css = #billing_first_name'
    last_name_field = 'css = #billing_last_name'
    phone_num_field = 'css = #billing_phone'
    email_field = 'css = #billing_email'

    delivery_checkbox1 = 'css = #shipping_method_0_local_pickup8'
    delivery_checkbox2 = 'css = #shipping_method_0_local_pickup10'
    delivery_checkbox3 = 'css = #shipping_method_0_local_pickup11'

    append_btn = 'css = div > button.cclwplus'
    subtract_btn = 'css = div > button.cclwminus'

    total_price_block = 'css = tr:nth-child(1) > td.total > span > span'

    submit_order_btn = 'css = #place_order'

    order_warning = 'css = div.woocommerce-NoticeGroup.woocommerce-NoticeGroup-checkout > ul'


# 12. Making order
class OrderCreation:
    def santos_making_order(self):
        sl.maximize_browser_window()
        bi.run_keyword('Mouse over', NavigationLocators.nav_panel_store)
        bi.run_keyword('Click link', NavigationLocators.nav_droplist_weight)
        bi.run_keyword('Mouse over', ProductItemLocators.santos)
        bi.run_keyword('Click link', Order_Locators.options_btn_santos)
        bi.run_keyword('Click element', CartLocators.options_droplist)
        bi.run_keyword('Click element', CartLocators.options_droplist_item3)
        bi.run_keyword('Clear element text', CartLocators.quantity_input)
        bi.run_keyword('Input text', CartLocators.quantity_input, '2')
        bi.run_keyword('Click element', CartLocators.opt_add_to_cart_btn)
        bi.run_keyword('Click element', CartLocators.cart_redirect_btn)

    def check_quantity_and_price(self):
        bi.run_keyword('Click button', Order_Locators.append_btn)
        bi.run_keyword('Wait until element contains', Order_Locators.total_price_block, '140,00')
        bi.run_keyword('Click button', Order_Locators.append_btn)
        bi.run_keyword('Wait until element contains', Order_Locators.total_price_block, '210,00')
        bi.run_keyword('Click button', Order_Locators.append_btn)
        bi.run_keyword('Wait until element contains', Order_Locators.total_price_block, '280,00')

    def add_chocolate_balsam_in_cart(self):
        sl.maximize_browser_window()
        bi.run_keyword('Mouse over', NavigationLocators.nav_panel_store)
        bi.run_keyword('Click link', NavigationLocators.nav_droplist_souvenirs)
        bi.run_keyword('Scroll element into view', CartLocators.souvenir_add_to_cart_btn)
        bi.run_keyword('Mouse over', ProductItemLocators.chocolate_balsam)
        bi.run_keyword('Click link', CartLocators.souvenir_add_to_cart_btn)
        bi.run_keyword('Click element', CartLocators.cart_redirect_btn)

    def order_user_data_input(self):
        bi.run_keyword('Input text', Order_Locators.name_field, UserData.user_name)
        bi.run_keyword('Input text', Order_Locators.last_name_field, UserData.user_last_name)
        bi.run_keyword('Input text', Order_Locators.phone_num_field, UserData.user_phone_num)
        bi.run_keyword('Input text', Order_Locators.email_field, UserData.user_email)

    def order_user_data_bad_input(self):
        bi.run_keyword('Input text', Order_Locators.name_field, UserData.bad_name)
        bi.run_keyword('Input text', Order_Locators.phone_num_field, UserData.bad_phone_num)
        bi.run_keyword('Input text', Order_Locators.email_field, UserData.bad_email)
    # 12. Making order
    def making_order(self):
        bi.run_keyword('santos_making_order')
        bi.run_keyword('order_user_data_input')
        bi.run_keyword('Click link', CartLocators.remove_sign)
        # ----- Test requires user intervention ---- #

    # 13. Making multi order
    def making_multi_order(self):
        sl.maximize_browser_window()
        bi.run_keyword('Mouse over', NavigationLocators.nav_panel_store)
        bi.run_keyword('Click link', NavigationLocators.nav_droplist_weight)
        bi.run_keyword('Mouse over', ProductItemLocators.burundi)
        bi.run_keyword('Click link', Order_Locators.option_btn_burundi)
        bi.run_keyword('Click element', CartLocators.options_droplist)
        bi.run_keyword('Click element', CartLocators.options_droplist_item8)
        bi.run_keyword('Clear element text', CartLocators.quantity_input)
        bi.run_keyword('Input text', CartLocators.quantity_input, '6')
        bi.run_keyword('Click element', CartLocators.opt_add_to_cart_btn)
        bi.run_keyword('Mouse over', NavigationLocators.nav_panel_store)
        bi.run_keyword('Click link', NavigationLocators.nav_droplist_souvenirs)
        bi.run_keyword('Mouse over', ProductItemLocators.keychain)
        bi.run_keyword('Click link', Order_Locators.option_btn_keychain)
        bi.run_keyword('Click element', CartLocators.options_droplist_keychain)
        bi.run_keyword('Click element', CartLocators.opt_add_to_cart_btn)
        bi.run_keyword('Click element', CartLocators.cart_redirect_btn)
        bi.run_keyword('order_user_data_input')
        bi.run_keyword('Click element', Order_Locators.delivery_checkbox1)
        # ----- Test requires user intervention ---- #

    # 14. Making order via "Nova Poshta" (Courier)
    def order_via_np_courier(self):
        bi.run_keyword('add_chocolate_balsam_in_cart')
        bi.run_keyword('order_user_data_input')
        bi.run_keyword('Click element', Order_Locators.delivery_checkbox2)
        # ----- Test requires user intervention ---- #

    # 15. Making order via UkrPoshta
    def order_via_ukr_poshta(self):
        bi.run_keyword('add_chocolate_balsam_in_cart')
        bi.run_keyword('check_quantity_and_price')
        bi.run_keyword('order_user_data_input')
        bi.run_keyword('Click element', Order_Locators.delivery_checkbox3)
        # ----- Test requires user intervention ----- #

    # 16. Making order wrong data
    def order_wrong_data(self):
        bi.run_keyword('santos_making_order')
        bi.run_keyword('order_user_data_bad_input')
        bi.run_keyword('Click button', Order_Locators.submit_order_btn)
        bi.run_keyword('Wait until page contains element', Order_Locators.order_warning)
