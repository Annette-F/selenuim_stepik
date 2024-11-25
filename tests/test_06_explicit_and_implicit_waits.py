from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time

'''
Implicit Waits - неявные ожидания. Неявное ожидание называется так, потому что его не нужно указывать отдельно, как time.sleep().

WebDriverWait — это класс из библиотеки Selenium, который используется для реализации явных ожиданий.

Implicit Wait — это время, которое Selenium будет ждать по умолчанию перед тем как выбросить исключение, если он не может найти элемент. 
Это как бы глобальный таймер, который применяется ко всем операциям поиска элементов.

.title_is(title) - ожидание проверки заголовка страницы. title - ожидаемый заголовок, который должен быть точным совпадением, 
возвращает True, если заголовок совпадает, в противном случае - false.

.title_contains(title) - вернёт true если title совпадает частично.
'''

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/expectations/1/index.html')
    element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    time.sleep(3)
    print(browser.find_element(By.ID, 'result').text)

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/expectations/2/index.html')
    browser.find_element(By.ID, "btn").click()
    element = WebDriverWait(browser, 10).until(EC.title_is('title changed'))
    print(element)

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/expectations/2/index.html')
    element = WebDriverWait(browser, 10).until(EC.title_contains('tle'))
    print(element)


'''
Проверка URL и заголовков

1. .title_is(title: str) - Это ожидаемое условие, которое проверяет, совпадает ли текущий заголовок веб-страницы с предоставленным значением.

title - ожидаемый заголовок страницы.

# Ожидание, пока заголовок страницы станет "My Page Title"
WebDriverWait(driver, 10).until(EC.title_is("My Page Title"))

2. .title_contains(title: str)— Это ожидаемое условие, которое проверяет, содержит ли текущий заголовок веб-страницы заданное подстроковое значение.

title - подстрока, которую должен содержать заголовок.

# Ожидание, пока заголовок страницы будет содержать "Page"
WebDriverWait(driver, 10).until(EC.title_contains("Page"))

3. .url_contains(url: str)— Это ожидаемое условие, которое проверяет, содержит ли текущий URL веб-страницы заданное подстроковое значение.

url - подстрока, которую должен содержать URL.

# Допустим, у вас есть следующая ссылка (URL) на веб-сайт:
https://www.example.com/dashboard/

# Если вы используете метод EC.url_contains("dashboard"), он вернет True для этой ссылки, потому что строка "dashboard" содержится в URL.

# Ожидание, пока URL будет содержать "dashboard"
WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))

4. .url_matches(pattern: str)— Это ожидаемое условие, которое проверяет, соответствует ли текущий URL страницы заданному регулярному выражению.

pattern- регулярное выражение для проверки URL.

# Ожидание, пока URL соответствует шаблону
WebDriverWait(driver, 10).until(EC.url_matches(r"https://www\.example\.com/[0-9]{4}/"))

4. .url_to_be(url: str)— Это ожидаемое условие, которое убеждается, что текущий URL веб-страницы точно совпадает с предоставленным значением.

url - ожидаемый URL страницы.

# Ожидание, пока URL станет "https://www.example.com"
WebDriverWait(driver, 10).until(EC.url_to_be("https://www.example.com"))

5. .url_changes(url: str)— Это ожидаемое условие, которое проверяет, отличается ли текущий URL веб-страницы от предоставленного значения.

url - исходный URL для сравнения.

# Ожидание, пока URL изменится относительно "https://www.example.com"
WebDriverWait(driver, 10).until(EC.url_changes("https://www.example.com"))
'''

'''
Проверка видимости и присутствия элементов в HTML

1. .presence_of_element_located(locator)— Это одно из ожидаемых условий , которое помогает нам убедиться, что элемент присутствует на веб-странице.

locator— кортеж, содержащий два элемента: тип поиска (By.ID, By.XPATH и т. д.) и значение для поиска.

locator = driver.find_element(By.ID, 'some_element_id') / (locator = (By.ID, 'some_element_id'))
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))

2. .visibility_of_element_located(locator)— Это одно из ожидаемых условий, позволяющее убедиться, что элемент не только присутствует на странице, но и видим пользователю.

locator— такой же, как и выше

locator = driver.find_element(By.XPATH, '//div[@class="visible_class"]') / (locator = (By.ID, 'some_element_id'))
element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))

3. .visibility_of(element)— Это условие ожидания, которое проверяет, является ли конкретный элемент видимым на веб-странице.

element— это уже найденный элемент Selenium.

element = driver.find_element(By.ID, 'visible_element_id') / (locator = (By.ID, 'some_element_id'))
visible_element = WebDriverWait(driver, 10).until(EC.visibility_of(element))

4. .presence_of_all_elements_located(locators)— В некоторых ситуациях вам может потребоваться работать не с одним элементом, а с группой элементов, например, со списком или рядом кнопок. Используя это условие, вы можете удостовериться, что все эти элементы загрузились и присутствуют на странице перед тем, как начать с ними взаимодействие. Метод проверяет наличие всех элементов, указанных локатором, в DOM-структуре страницы. Однако стоит помнить, что "присутствие" не гарантирует "видимость" элемента.

locator — такой же, как и выше.

locator = driver.find_elements(By.CLASS_NAME, 'some_class_name') / (locator = (By.ID, 'some_element_id'))
elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(locator))

5. .visibility_of_any_elements_located(locator)— Это ожидаемое условие, которое проверяет видимость хотя бы одного элемента из группы элементов, соответствующих заданному локатору.

locator — такой же, как и выше.

locator = driver.find_element(By.TAG_NAME, 'li') / (locator = (By.ID, 'some_element_id'))
visible_elements = WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located(locator))

6. .visibility_of_all_elements_located(locator)— Это ожидаемое условие в, которое убеждается в том, что абсолютно все элементы, соответствующие указанному локатору, являются видимыми на веб-странице.

locator — такой же, как и выше.

locator = driver.find_element(By.CSS_SELECTOR, '.visible_elements') / (locator = (By.ID, 'some_element_id'))
all_visible_elements = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(locator))
'''