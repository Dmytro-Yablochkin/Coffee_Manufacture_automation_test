*** Settings ***
Documentation    Test for site functionality

Library    SeleniumLibrary
Library    manufacture/RegistrationForm.py
Library    manufacture/AuthorizationForm.py
Library    manufacture/NavPageFunctionality.py
Library    manufacture/CartFunctionality.py
Library    manufacture/OrderCreation.py
Library    manufacture/OtherSiteInfo.py
Library    manufacture/Links.py

Test Setup    Open Browser  ${MAIN_PAGE_URL}   chrome
Test Teardown    Close all browsers

*** Variables ***
${MAIN_PAGE_URL}    https://manufacture.coffee/


*** Test Cases ***
# REGISTRATION
# ----- Test requires user intervention ---- #
1. Customer registration
    Fill registration form
2. "Check user can navigate to registration form with empty Email adress field"
    Empty field registration form

# AUTHORIZATION/LOGOUT

3. Authotization
    Authorization
4. Authotization: With wrong email, Empty password field
    Authorization bad test1
5. Authorization: With empty email field, Wrong password
    Authorization bad test2
6. Logout
    Log out


# OTHER PAGE FUNCTIONALITY
7. Auto-scroll button
    Auto scroll btn
8. Photo scrolling button right/left
    Click right and left btns
9. Navigation panel droplist
    Hover on nav item

# CART FUNCTIONALITY
10. Addings item to cart
    Add item
11. Delete item from the cart
    Delete item

# ORDER CREATION
12. Making order
    Making order
13. Making multi order
    Making multi order
14. Making order via "Nova Poshta" (Courier)
    Order via NP courier
15. Making order via UkrPoshta
    Order via ukr poshta
16. Making order wrong data
    Order wrong data

# OTHER
17. Other site information
    Redirect to places page

# SOCIAL LINKS
18. Facebook link
    Click Facebook link
19. Instagram link
    Click Instagram link

#OTHER CART FUNCTIONALITY
20. Item scroll button Left/Right
    Top sells block btns

21. Saving shopping cart information functionality
    Create and refresh
