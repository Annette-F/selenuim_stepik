import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Вкладки в браузере
'''
Дескрипторы — это те сущности, которые помогают нам манипулировать вкладками

.current_window_handle — возвращает дескриптор текущей вкладки;
.window_handles — возвращает список всех дескрипторов открытых вкладок;
.switch_to.window(window_handles[0]) — переключает фокус между вкладками.
'''


def test_descriptors():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/blank/2/1.html')
        time.sleep(1)
        browser.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank1");')
        browser.execute_script('window.open("http://parsinger.ru/blank/2/3.html", "_blank2");')
        browser.execute_script('window.open("http://parsinger.ru/blank/2/4.html", "_blank3");')
        time.sleep(2)
        print(browser.window_handles)


def test_tabs():
    with webdriver.Chrome() as browser:
        # browser.get("https://stepik.org/course/104774/promo") # Вместо вкладки data; будет вкладка в которой будет загружен степик
        browser.execute_script('window.open("http://parsinger.ru/blank/2/1.html", "_blank1");')
        browser.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank2");')
        browser.execute_script('window.open("http://parsinger.ru/blank/2/3.html", "_blank3");')
        browser.execute_script('window.open("http://parsinger.ru/blank/2/4.html", "_blank4");')

        for x in range(
                len(browser.window_handles)):  # reversed(range(len(browser.window_handles))) Для итерирования по порядку
            browser.switch_to.window(browser.window_handles[x])
            for y in browser.find_elements(By.CLASS_NAME, 'check'):
                y.click()


def test_tabs_iterations():
    with webdriver.Chrome() as browser:
        time.sleep(1)
        browser.execute_script('window.open("http://parsinger.ru/blank/0/1.html", "_blank1");')
        browser.execute_script('window.open("http://parsinger.ru/blank/0/2.html", "_blank2");')
        browser.execute_script('window.open("http://parsinger.ru/blank/0/3.html", "_blank3");')
        browser.execute_script('window.open("http://parsinger.ru/blank/0/4.html", "_blank4");')
        browser.execute_script('window.open("http://parsinger.ru/blank/0/5.html", "_blank5");')
        browser.execute_script('window.open("http://parsinger.ru/blank/0/6.html", "_blank6");')

        for x in range(len(browser.window_handles)):
            browser.switch_to.window(browser.window_handles[x])
            time.sleep(1)
            print(browser.execute_script("return document.title;"), browser.window_handles[x])


# Получаем title вкладки

'''
Title — это то, что содержится в HTML-тегах <title>Текст на вкладке</title> и отображается на вкладке браузера.

.execute_script("return document.title;") - получить имя вкладки
'''


def test_get_title():
    with webdriver.Chrome() as browser:
        browser.get("https://stepik.org/course/104774/promo")
        print(browser.execute_script("return document.title;"))


# Размеры окна браузера

'''
1. driver.set_window_size(X, Y) - Задать размер окна браузера.
Где X – это ширина окна;
Где Y – это высота окна.

2. driver.get_window_size() - Получить размер окна браузера

3. .get_window_size().get('height'):

.get('height'): Метод get — это альтернативный способ извлечения значения из словаря. Он вернет значение, соответствующее ключу 'height', или None, если такого ключа нет в словаре. 
В данном контексте это выражение также вернет высоту окна браузера. 

4. .get_window_size().get('width'):

.get('width'): Метод get извлекает значение из словаря по ключу 'width'. Таким образом, это выражение вернет ширину окна браузера. 

5. get_window_size()["width"]:

["width"]: Это обращение к значению словаря по ключу "width". Это выражение вернет ширину окна браузера.

6. .get_window_size()["height"]:

["height"]: Это обращение к значению словаря по ключу "height". Это выражение вернет высоту окна браузера.
'''

# Модальные окна

'''
Модальное окно — это окно, которое блокирует работу пользователя до тех пор, пока это окно не закроют. 

Основные функции применяемые к модальным окнам.

1. .switch_to - позволяет переключить фокус на модальное окно. Это необходимо, чтобы взаимодействовать с содержимым этого окна.

# Переключение фокуса на модальное окно
driver.switch_to.alert

2. .accept() - имитирует нажатие на кнопку "ОК" в модальном окне. Обычно используется для подтверждения какого-либо действия.

# Подтвердить содержимое модального окна
driver.switch_to.alert.accept()

3. .dismiss() - имитирует нажатие на кнопку "Отмена" в модальном окне. Позволяет отказаться от выполнения какого-либо действия или закрыть окно без подтверждения.

# Или отклонить содержимое модального окна
driver.switch_to.alert.dismiss()

6. .send_keys() - позволяет отправить текст в текстовое поле внутри модального окна. Например, это может быть поле для ввода пароля или комментария.

# Отправка текста в текстовое поле модального окна
driver.switch_to.alert.send_keys("Текст для отправки")

7. .text - возвращает заголовок (title) модального окна. Это может пригодиться для проверки того, что правильное окно отображается на экране.

# Получение title модального окна
modal_title = driver.switch_to.alert.text
'''


def test_modal_windows_alert():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/blank/modal/1/index.html')
        browser.find_element(By.ID, 'alert').click()
        time.sleep(1)
        alert = browser.switch_to.alert  # Если вы планируете что-то делать с этим событием, можно добавить его в переменную
        print(alert.text)
        time.sleep(1)
        alert.accept()
        time.sleep(1)


def test_modal_windows_promp():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/blank/modal/1/index.html')
        browser.find_element(By.ID, 'prompt').click()
        time.sleep(2)
        prompt = browser.switch_to.alert
        prompt.send_keys('Введёный текст')
        prompt.accept()
        time.sleep(.5)
        print(browser.find_element(By.ID, 'result').text)
        time.sleep(1)


def test_modal_windows_confirm():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/blank/modal/1/index.html')
        browser.find_element(By.ID, 'confirm').click()
        time.sleep(2)
        prompt = browser.switch_to.alert
        prompt.accept()  # Замените на .dismiss() чтобы нажать на кнопку "Отмена"
        time.sleep(.5)


# Работа с фреймами iframe

'''
driver.switch_to.frame(iframe) 

Способы переключения на фрейм:

1. Используя WebElement: Это наиболее гибкий вариант. Вы можете найти фрейм с помощью вашего предпочтительного селектора и переключиться на него.
iframe = driver.find_element(By.CSS_SELECTOR, "#modal > iframe")
driver.switch_to.frame(iframe)
driver.find_element(By.TAG_NAME, 'button').click()

2. Используя имя или ID: Если у вашего фрейма или iFrame есть атрибуты id или name, вы можете использовать их.
driver.switch_to.frame('buttonframe')
driver.find_element(By.TAG_NAME, 'button').click()
 
3. Используя индекс: Также можно использовать индекс фрейма.
driver.switch_to.frame(1)
 
4. Выход из фрейма: Чтобы выйти из iFrame или frameset, вернитесь к содержимому по умолчанию.
driver.switch_to.default_content()

Зачем нужен выход из фрейма?

1. Ограниченная область видимости: Когда вы находитесь внутри фрейма (или iFrame), ваша область видимости ограничена только этим фреймом. 
Это означает, что вы не можете взаимодействовать с элементами вне этого фрейма.

2. Взаимодействие с основным содержимым: После завершения работы внутри фрейма, вам, возможно, потребуется взаимодействовать с элементами основного документа. 
Чтобы это сделать, вы должны выйти из фрейма.

3. Переключение между фреймами: Если на странице есть несколько фреймов и вам нужно переключиться с одного фрейма на другой, 
вы сначала должны вернуться к основному содержимому, прежде чем переключиться на другой фрейм.

4. Избегание ошибок: Если вы пытаетесь взаимодействовать с элементом, который находится вне текущего фрейма, 
без выхода из этого фрейма, вы получите ошибку, такую как "NoSuchElementException". 
Чтобы избежать таких ошибок, важно знать, в каком контексте (фрейме) вы находитесь, и при необходимости выходить из него.
'''


def test_get_iframe():
    with webdriver.Chrome() as driver:
        driver.get('https://parsinger.ru/selenium/5.8/4/index.html')

        # Переключаемся на iframe
        iframe_element = driver.find_element(By.TAG_NAME, 'iframe')
        driver.switch_to.frame(iframe_element)

        # Извлекаем HTML содержимое из iframe
        iframe_content = driver.page_source

        print(iframe_content)


'''
Task 1:
Задание
Запуск: Откройте указанный веб-сайт с использованием Selenium.

Исследование: На странице размещено 100 кнопок. Отправьтесь в путешествие, кликая по каждой из них, чтобы понять, какая из них прячет желаемый код.

Обнаружение: При активации правильной кнопки, секретный код появится в теге: <p id="result">Code</p>.

Финальный штрих: Скопируйте этот код и вставьте его в специальное поле для ответа на степик.
'''
def test_task_1():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/5.8/1/index.html')
        for button in browser.find_elements(By.CLASS_NAME, 'buttons'):
            button.click()
            browser.switch_to.alert.accept()
            text = browser.find_element(By.ID, 'result').text
            if text:
                print(text)
                break


'''
Task 2:
Задание:

Доступ к месту преступления: Используйте Selenium, чтобы получить доступ к веб-сайту, где спрятаны улики.

Внимательное расследование: На сайте находится 100 кнопок. Каждая из них при нажатии активирует всплывающее alert окно с пин-кодом.

Расшифровка: Под кнопками расположено текстовое поле, которое проверяет пин-коды. Ваша задача — ввести пин-код и проверить его. 
Если пин-код верный, вы получите секретный код.

'''

def test_tast_2():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/5.8/2/index.html')
        button = browser.find_elements(By.CLASS_NAME, 'buttons')
        for i in button:
            i.click()
            pin = browser.switch_to.alert.text
            alert = browser.switch_to.alert
            alert.accept()
            browser.find_element(By.ID, 'input').send_keys(pin)
            browser.find_element(By.XPATH, '//input[@value="Проверить"]').click()
            alert = browser.find_element(By.ID, 'result').text
            if 'Неверный пин-код' not in alert:
                print(alert)


'''
Task 3:
Цель
Место преступления: Откройте указанный сайт с помощью Selenium.

Улики на месте: На сайте вы найдете список пин-кодов. Однако среди них лишь один правильный.

Расшифровка: Для проверки каждого пин-кода используйте кнопку "Проверить". При верном пин-коде вы получите секретный код.

Доклад о проведенной работе: Вставьте полученный секретный код в специальное поле для на степик.
'''

def test_task_3():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/5.8/3/index.html')
        pin_codes = browser.find_elements(By.CLASS_NAME, 'pin')
        for pin in pin_codes:
            extracted_text = pin.text
            browser.find_element(By.TAG_NAME, 'input').click()
            check = browser.switch_to.alert
            check.send_keys(extracted_text)
            check.accept()
            alert = browser.find_element(By.ID, 'result').text
            if 'Неверный пин-код' not in alert:
                print(alert)


'''
Task 4
Цель: Проанализировать содержимое сайта, имея строгие рамки видимой области браузера.

Шаги к решению:

Инициализация: Запустите браузер через Selenium и загрузите страницу.
Настройка размеров: Откройте окно браузера так, чтобы рабочая (видимая) область страницы точно соответствовала 555x555 пикселям. Не забудьте учесть размеры рамок и панелей браузера при расчете!
Анализ: Когда условие будет выполнено секретный ключ появится в id="result";
Действие: Извлеките содержимое данного элемента и вставьте в поле для ответа.
'''

def test_task_4():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/window_size/1/')
        browser.set_window_size(555 + 16, 555 + 147)
        result = browser.find_element(By.ID, 'result').text
        print(result)


'''
Task 5
Шаги к решению:

Погружение: Откройте сайт с помощью Selenium.
Активация тайных порталов: Нажимая на каждую из 10 кнопок, вы активируете ворота в другую вкладку. Это ваш шанс найти одну из частей кода.
Исследование: В каждой новой вкладке ищите в title число — ваш ключ к решению.
Сбор информации: Соберите все 10 чисел и сложите их.
Завершение миссии: Вставьте итоговую сумму в поле для ответа на исходной странице.
'''

def test_task_6():
    with webdriver.Chrome() as browser:
        count = 0
        browser.get('https://parsinger.ru/blank/3/index.html')
        buttons = browser.find_elements(By.CLASS_NAME, 'buttons')
        for button in buttons:
            button.click()
        windows = browser.window_handles
        for window in windows[1:]:
            browser.switch_to.window(window)
            count += int(browser.execute_script("return document.title;"))
        print(count)
