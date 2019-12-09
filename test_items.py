import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_should_exists(browser):
    browser.get(link)
    time.sleep(3)
    assert len(browser.find_elements_by_css_selector(".btn-add-to-basket")) != 0, "button not found"