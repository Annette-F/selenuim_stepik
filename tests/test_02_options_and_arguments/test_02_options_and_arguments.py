from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_1():
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('--headless')
    with webdriver.Chrome(options=options_chrome) as browser:
        url = 'https://stepik.org/course/104774'
        browser.get(url)

        a = browser.find_element(By.TAG_NAME, 'a')
        print(a.get_attribute('href'))


# Proxy and Selenium
def test_2():
    url = 'https://2ip.ru/'
    with webdriver.Chrome() as browser:
        browser.get(url)
        time.sleep(5)
        print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
        time.sleep(5)


def test_3():
    proxy = '199.60.103.28:80'
    url = 'https://2ip.ru/'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % proxy)
    with webdriver.Chrome(options=chrome_options) as browser:
        browser.get(url)
        print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)
        time.sleep(5)


def test_4():
    proxy_list = ['8.210.83.33:80', '199.60.103.28:80',
                  '103.151.246.38:10001', '199.60.103.228:80',
                  '199.60.103.228:80', '199.60.103.28:80', ]

    for PROXY in proxy_list:
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--proxy-server=%s' % PROXY)
            url = 'https://2ip.ru/'

            with webdriver.Chrome(options=chrome_options) as browser:
                browser.get(url)
                print(browser.find_element(By.ID, 'd_clip_button').find_element(By.TAG_NAME, 'span').text)

                browser.set_page_load_timeout(5)

                proxy_list.remove(PROXY)
        except Exception as _ex:
            print(f'Превышен timeout ожидания для - {PROXY}')
            continue


'''
# Some commands:

--disable-gpu - Отключает аппаратное ускорение GPU. Иногда это делается для избежания проблем с графикой.

--no-sandbox - Запускает браузер без дополнительных мер безопасности.

--incognito - Запускает браузер в режиме инкогнито. В этом режиме не сохраняются куки и история просмотров.

--window-size=width,height - Устанавливает начальный размер окна браузера.

--start-maximized - Запускает браузер на весь экран.

--disable-extensions - Отключает все установленные расширения.

--user-data-dir=path - Устанавливает директорию для хранения профиля пользователя.

--disable-infobars - Убирает информационные строки в верхней части окна.

--ignore-certificate-errors - Игнорирует ошибки SSL-сертификатов. Полезно, если нужно обращаться к сайтам с недействительными сертификатами.

--lang=ru - Устанавливает язык интерфейса браузера на русский.

--disable-popup-blocking - Отключает блокировку всплывающих окон. Может быть полезным при автоматизации некоторых сценариев.

--allow-running-insecure-content - Позволяет загружать небезопасный контент на страницы, загруженные по HTTPS. Опасная опция, используйте с осторожностью.

--disable-notifications - Отключает уведомления браузера. Особенно полезно при автоматизированном тестировании.

--disable-web-security - Отключает меры безопасности веба. Не рекомендуется для обычного просмотра, но может быть полезно для тестирования.

--disable-client-side-phishing-detection - Отключает обнаружение фишинга на клиентской стороне.

--enable-logging - Включает журналирование в файл.

--log-level=0 - Устанавливает уровень журналирования (0-3).

--disable-cache - Отключает кэш браузера. Полезно для тестирования изменений на веб-страницах в реальном времени.

--enable-automation - Подсказывает браузеру, что он управляется программой. Это может изменить поведение некоторых веб-сайтов.

--disable-setuid-sandbox - Отключает песочницу безопасности для браузера. Также не рекомендуется для обыденного использования.

--disable-sync - Отключает синхронизацию с аккаунтом Google.
'''
