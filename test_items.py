import time

def test_button_exist(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    found = True
    try:
        button = browser.find_element_by_css_selector(".btn-add-to-basket")
    except:
        found = False
    assert found






