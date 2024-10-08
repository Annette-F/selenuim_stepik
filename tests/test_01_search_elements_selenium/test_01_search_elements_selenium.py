import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By


def test_1():
    with webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install())) as driver:
        driver.get("https://stepik.org/course/104774")
        time.sleep(5)


'''
# Search elements in Selenium

# 1. By.ID
element_id = driver.find_element(By.ID, 'some_id')

# 2. By.CSS_SELECTOR
elements_css_selector = driver.find_elements(By.CSS_SELECTOR, '.some_class')

# 3. By.XPATH
element_xpath = driver.find_element(By.XPATH, '//div[@attribute="value"]')

# 4. By.NAME
element_name = driver.find_element(By.NAME, 'username')

# 5. By.TAG_NAME
images_tag_name = driver.find_elements(By.TAG_NAME, 'img')

# 6. By.CLASS_NAME
buttons_class_name = driver.find_elements(By.CLASS_NAME, 'btn')

# 7. By.LINK_TEXT
element_link_text = driver.find_element(By.LINK_TEXT, 'Continue')

# 8. By.PARTIAL_LINK_TEXT
element_partial_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, 'Cont')
'''


# Example code with search element and click on it:
def test_2():
    browser = webdriver.Chrome()
    browser.get('http://parsinger.ru/html/watch/1/1_1.html')
    browser.find_element(By.ID, "sale_button").click()

    time.sleep(10)


'''
# Some methods of WebElement

# 1. .click()
browser.find_element(By.ID, 'some_button_id').click()

# 2. .send_keys()
browser.find_element(By.NAME, 'some_textbox_name').send_keys('Hello, World!')

# 3. .get_attribute('some_attribute')
browser.find_element(By.TAG_NAME, 'a').get_attribute('href')

# 4. .text
browser.find_element(By.CLASS_NAME, 'some_class_name').text
'''


# Work with browser:
def test_3():
    # Example 1:
    driver = webdriver.Chrome()
    driver.get('http://parsinger.ru/html/watch/1/1_1.html')
    button = driver.find_element(By.ID, "sale_button")
    time.sleep(2)
    button.click()
    time.sleep(2)

    driver.quit()


def test_4():
    # example 2:
    try:
        driver = webdriver.Chrome()
        driver.get('http://parsinger.ru/html/watch/1/1_1.html')
        button = driver.find_element(By.ID, "sale_button")
        time.sleep(2)
        button.click()
        time.sleep(2)
    finally:
        driver.quit()


def test_5():
    # example 3:
    with webdriver.Chrome() as driver:
        driver.get('http://parsinger.ru/html/watch/1/1_1.html')
        button = driver.find_element(By.ID, "sale_button")
        time.sleep(2)
        button.click()
        time.sleep(2)
