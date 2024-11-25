from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

'''
# Навигация по истории браузера:

1. webdriver.back() - вернуться на предыдущую страницу в браузере.

2. webdriver.forward() - перемещает вперёд по истории браузера.

3. webdriver.refresh() - обновляет текущую страницу в браузере.
'''

'''
# Работа со скриншотами:

1. webdriver.get_screenshot_as_file("../file_name.jpg") - Сохраняет скриншот страницы в файл по указанному пути. 
Возвращает True если всё прошло успешно, и False при ошибках ввода-вывода.

2. webdriver.save_screenshot("file_name.jpg") - Сохраняет скриншот в папке с проектом.

3. webdriver.get_screenshot_as_png() - Возвращает скриншот в виде двоичных данных (binary data), 
которые можно передать или сохранить в файл в конструкторе with/as.

4. webdriver.get_screenshot_as_base64() - Возвращает скриншот в виде строки в кодировке Base64. Удобно для встроенных изображений в HTML.
'''

'''
# Открытие и закрытие страниц и браузера:

1. webdriver.get("http://example_url.ru") - Открывает указанный URL в браузере.

2. webdriver.quit() - Закрывает все вкладки и окна, завершает процесс драйвера, освобождает ресурсы.

3. webdriver.close() - Закрывает только текущую вкладку.
'''

'''
# Исполнение JavaScript:

1. webdriver.execute_script("script_code") - Выполняет JavaScript код на текущей странице.

2. webdriver.execute_async_script("script_code" , *args ) - Асинхронно выполняет JavaScript код. Удобно для работы с AJAX и промисами.
'''

'''
# Время ожидания:

1. webdriver.set_page_load_timeout() - Устанавливает таймаут на загрузку страницы. Выбрасывает исключение, если время вышло.
'''

'''
# Поиск элементов:

1. webdriver.find_element(By.ID, 'example_id') - Возвращает первый найденный элемент по заданному локатору.

2. webdriver.find_elements(By.ID, 'example_id') - Возвращает список всех элементов, соответствующих локатору.
'''

'''
# Работа с окном браузера:

1. webdriver.get_window_position() - Возвращает словарь с текущей позицией окна браузера ({'x': 10, 'y': 50}).

2. webdriver.maximize_window() - Разворачивает окно на весь экран.

3. webdriver.minimize_window() - Сворачивает окно.
 
4. webdriver.fullscreen_window()  - Переводит окно в полноэкранный режим, как при нажатии F11.
 
5. webdriver.get_window_size() - Возвращает размер окна в виде словаря ({'width': 945, 'height': 1020}).
 
6. webdriver.set_window_size(800,600) - Устанавливает новый размер окна.
'''

'''
# Работа с cookies:

1. webdriver.get_cookies()  - Возвращает список всех cookies.
 
2. webdriver.get_cookie(name_cookie) - Возвращает конкретную cookie по имени.
 
3. webdriver.add_cookie(cookie_dict) - Добавляет новую cookie к вашему текущему сеансу.
 
4. webdriver.delete_cookie(name_cookie) - Удаляет cookie по имени.
 
5. webdriver.delete_all_cookies() - удаляет все файлы cookie в рамках текущего сеанса.
'''

'''
# Ожидание элементов:

1. webdriver.implicitly_wait(10) - Устанавливает неявное ожидание на поиск элементов или выполнение команд.
 
2. webdriver.WebDriverWait(driver, timeout).until(condition)
'''

'''
# Работа с элементами:

1. element.click() - Симулирует клик по элементу.

2. element.send_keys("text") - Вводит текст в текстовое поле. Очень полезно для автоматизации ввода данных.

3. element.clear() - Очищает текстовое поле.

4. element.is_displayed() - Проверяет, отображается ли элемент на странице.

5. element.is_enabled() - Проверяет, доступен ли элемент для взаимодействия (например, не заблокирован).

6. element.is_selected() - Проверяет, выбран ли элемент (актуально для радиокнопок и чекбоксов).

7. element.get_attribute("attribute") - Возвращает значение указанного атрибута элемента.

8. element.text - Возвращает текст элемента.

9. element.submit() - Отправляет форму, в которой находится элемент.
'''

'''
# Фреймы:

1. webdriver.switch_to.frame("frame_name") - Переключает фокус на указанный фрейм.

2. webdriver.switch_to.default_content() - Возвращает фокус на основное содержимое страницы, выходя из фрейма.
'''

'''
# JavaScript Alerts:

1. webdriver.switch_to.alert - Переключает фокус на всплывающее окно JavaScript.
'''


# .get_cookies()
def test_get_cookies():
    browser = webdriver.Chrome()
    browser.get('https://ya.ru/')
    cookies = browser.get_cookies()
    print(cookies)


def test_get_name_cookies():
    browser = webdriver.Chrome()
    browser.get('https://ya.ru/')
    cookies = browser.get_cookies()
    for cookie in cookies:
        print(cookie['name'])  # или cookie['value'] чтобы получить их значение


def test_get_value_cookie():
    browser = webdriver.Chrome()
    browser.get('https://ya.ru/')
    print(browser.get_cookie('Session_id')['expiry'])


# .add_cookie(cookie_dict)
'''
# Добавляет файл cookie в текущий контекст браузера:

driver.add_cookie({"name": "key", "value": "value"})

1. "name" — устанавливает имя cookie-файла.
 
2. "value" — устанавливает значение cookie; это значение может либо идентифицировать пользователя, либо содержать любую другую служебную информацию.
 
3. "expires" и "max-age" — определяют срок жизни cookie; после истечения этого срока, cookie будет удалён из памяти браузера. 
Если не указывать эти значения, содержимое cookie будет удалено после закрытия браузера.
 
4. "path" — указывает путь к директории на сервере, для которой будут доступны cookie. Чтобы cookie были доступны по всему домену, необходимо указать "/".
 
5. "domain" — хранит в себе информацию о домене или поддомене, которые имеют доступ к этой cookie. 
Если необходимо, чтобы cookie были доступны по всему домену и всем поддоменам, указывается базовый домен, например, www.example.ru.
 
6. "secure" — указывает серверу, что cookie должны передаваться только по защищённому HTTPS-соединению.
 
7. "httponly"— этот параметр запрещает доступ к cookie посредством API браузера document.cookie. 
Предотвращает кражу cookie посредством XSS-атак. Если флаг установлен в True, вы сможете получить доступ к этой cookie только через браузер, 
в том числе и через Selenium.
 
8. "samesite"— ограничивает передачу cookie между сайтами и предотвращает кражу cookie посредством XSS-атак. Имеет три состояния:

 - SameSite=None — на передачу cookie нет никаких ограничений;
 - SameSite=Lax — разрешает передачу только безопасным HTTP-методам;
 - SameSite=Strict или SameSite — самое строгое состояние, которое запрещает отправку cookie на другие сайты.
'''


def test_add_cookie():
    cookie_dict = {
        'name': 'any_name_cookie',  # Любое имя для cookie
        'value': 'any_value_cookie',  # Любое значение для cookie
        'expiry': 2_000_000_000,  # Время жизни cookie в секундах
        'path': '/',  # Директория на сервере дял которой будут доступны cookie
        'domain': 'parsinger.ru',  # Информация о домене и поддомене для которых доступны cookie
        'secure': True,  # or False   # Сигнал браузера о том что передать cookie только по защищённому HTTPS
        'httpOnly': True,  # or False # Ограничивает достук к cookie по средствам API
        'sameSite': 'Strict',  # or lax or none # Ограничение на передачу cookie между сайтами
    }
    browser = webdriver.Chrome()
    browser.get('https://parsinger.ru/methods/4/index.html')
    browser.add_cookie(cookie_dict)
    print(browser.get_cookies())
    time.sleep(100)


# .execute_script(script, *args)
'''
1. .execute_script("return arguments[0].scrollIntoView(true);", element) — прокручивает родительский контейнер элемента таким образом, 
чтобы element, для которого вызывается scrollIntoView, был виден пользователю.

2. .execute_script("window.open('http://parsinger.ru', 'tab2');") — создаст новую вкладку в браузере с именем "tab2".

3. .execute_script("return document.body.scrollHeight") — вернёт значение высоты элемента <body>.

4. .execute_script("return window.innerHeight") — вернёт значение высоты окна браузера.

5. .execute_script("return window.innerWidth") — вернёт значение ширины окна браузера.

6. .execute_script("window.scrollBy(X, Y)") — прокрутит документ на заданное число пикселей по осям X и Y.

X — смещение в пикселях по горизонтали.
Y — смещение в пикселях по вертикали.

7. .execute_script("alert('Ура Selenium')") — вызывает модальное окно Alert.

8. .execute_script("return document.title;") — возвращает title открытого документа.

9. .execute_script("return document.documentURI;") — возвращает URL документа.

10. .execute_script("return document.readyState;") — возвращает состояние загрузки страницы; вернёт "complete", если страница загрузилась.

11. .execute_script("return document.anchors;") — возвращает список всех якорей на странице.

[x.tag_name for x in browser.execute_script("return document.anchors;")] — этот код позволяет получить список всех тегов с якорями. 
Очень полезная инструкция, особенно если при скроллинге элемент для "зацепления" не найден.

12. .execute_script("return document.cookie;") — возвращает строку, содержащую все cookies документа, разделённые точкой с запятой.

13. .execute_script("return document.domain;") — возвращает домен текущего документа.

14. .execute_script("return document.forms;") — возвращает список всех форм на странице.

15. .execute_script("window.scrollTo(x-coord, y-coord);") — прокручивает документ до указанных координат:

x-coord — позиция по горизонтальной оси, которая будет отображена вверху
y-coord — позиция по вертикальной оси, которая будет отображена вверху слева.

16. .execute_script("return document.getElementsByClassName('container');") — возвращает список всех элементов с классом 'container'.

17. .execute_script("return document.getElementsByTagName('container');") — возвращает список всех элементов с тегом 'container'.
 
18. .execute_script("return document.getElementById('some-id');") —  возвращает элемент с указанным ID 'some-id'.
'''

'''
Task 1:
Задачи
Прибытие на "Остров": Используйте Selenium для открытия заданного веб-сайта https://parsinger.ru/methods/1/index.html.

Охота на Сокровище: В элементе с id="result" иногда появляется число — это и есть ваше сокровище. Проблема в том, что оно появляется очень редко. Вам придется обновлять страницу множество раз, пока не увидите это число.

Клад в Руках: Как только число появится, скопируйте его и вставьте в предназначенное для этого поле ответа на вашем курсе.
'''


def test_task_1():
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('--headless')
    with webdriver.Chrome(options=options_chrome) as browser:
        browser.get('https://parsinger.ru/methods/1/index.html')
        result = browser.find_element(By.ID, 'result').text
        while result == 'refresh page':
            browser.refresh()
            result = browser.find_element(By.ID, 'result').text
        if result != 'refresh page':
            print(result)


'''
Task 2:
Задачи
На старт, внимание, марш!: Откройте указанную веб-страницу с помощью Selenium. 

Операция 'Чистый Лист': На странице расположены 100 текстовых полей с текстом. Ваша задача — пройтись по каждому и удалить его содержимое. Причём быстро, у вас всего 5 секунд!

Завершающий этап: После того как все поля будут очищены, нажмите на кнопку на странице.

Секретный Код: Скопируйте число, которое появится во всплывающем alert-окне, с помощью Selenium.

Результат: Вставьте полученное число в поле ответа степик.

Для очистки текстового поля используйте: 

field.clear()

Для переключения на alert-окно и получения текста из него, используйте:

# Переключаемся на алерт и получаем его текст
alert = driver.switch_to.alert.text
'''


def test_task_2():
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('--headless')
    with webdriver.Chrome(options=options_chrome) as browser:
        browser.get('https://parsinger.ru/selenium/5.5/1/1.html')
        fields = browser.find_elements(By.CLASS_NAME, 'text-field')
        for field in fields:
            field.clear()
        browser.find_element(By.ID, 'checkButton').click()
        print(browser.switch_to.alert.text)


'''
Task 3:
Этапы миссии:

Запустите ваш кибер-копатель и отправьтесь на заданный сайт.

Особая задача сбора: Соберите только те "печеньки", значения которых имеют чётные числа после символа "_". Например, если cookie имеет имя "session_12", число "12" является чётным, и это именно то, что вам нужно.

Анализ и суммирование: Суммируйте числовые значения этих особых "печенек". Это сумма будет вашим ключом.

Ввод ответа: После расшифровки вставьте ваш ключ в специальное поле для ответов на степик. Успех здесь означает ваш переход на следующий уровень задания.
'''


def test_task_3():
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('--headless')
    with webdriver.Chrome(options=options_chrome) as browser:
        browser.get('https://parsinger.ru/methods/3/index.html')
        cookies = browser.get_cookies()
        sum_cookies = 0
        for cookie in cookies:
            if int(cookie['name'].rsplit('_', 1)[-1]) % 2 == 0:
                sum_cookies += int(cookie['value'])
        print(sum_cookies)


'''
Task 4:
Задачи
Стартовая Позиция: Используя Selenium, откройте заданный веб-сайт. Убедитесь, что ваша машина готова к операции.

Секунды на Счетчике: У вас есть ровно 5 секунд, чтобы пройтись по ячейкам на странице и очистить только те, которые доступны для редактирования.

Проверка: Нажмите на кнопку "Проверить" на странице.

Секретный код: Из всплывающего алерт-окна скопируйте код и вставьте его в поле для ответа.

 

Для проверки доступности текстового поля, используйте проверку атрибута disabled у соответствующих текстовых полей:

.get_attribute('disabled')
'''


def test_task_4():
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('--headless')
    with webdriver.Chrome(options=options_chrome) as browser:
        browser.get('https://parsinger.ru/selenium/5.5/2/1.html')
        elements = browser.find_elements(By.CLASS_NAME, 'text-field')
        for element in elements:
            if not element.get_attribute('disabled'):
                element.clear()
        browser.find_element(By.ID, 'checkButton').click()
        print(browser.switch_to.alert.text)


'''
Task 5:
Этапы миссии:

Запуск: Откройте основной сайт с помощью Selenium. С этой точки начнётся ваша экспедиция в поисках "Бессмертного Печенюшка".

Следование за линками: На основной странице будет 42 ссылки. Открывайте каждую из них, чтобы исследовать и выяснить, какой из cookies имеет самый долгий срок жизни.

Вычисление жизнеспособности: Для каждой открытой страницы анализируйте срок жизни её cookie ['expiry']. Сохраняйте эти данные для последующего сравнения.

Коронация Бессмертного: После проверки всех 42 страниц определите, на какой из них находится cookie с самым долгим сроком жизни. С этой страницы извлеките число которое лежит в  теге <p id="result">INT</p>.

Завершающий этап: Вставьте полученное число в специальное поле для степик. Поздравляем, вы нашли "Бессмертного Печенюшка" и преуспели в этой миссии!
'''


def test_task_5():
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('--headless')
    with webdriver.Chrome(options=options_chrome) as browser:
        browser.get('https://parsinger.ru/methods/5/index.html')
        l_href = [item.get_attribute('href') for item in browser.find_elements(By.TAG_NAME, 'a')]
        expiry = 0
        result = 0
        for link in l_href:
            browser.get(link)
            cookies = browser.get_cookies()
            for key in cookies:
                if key['expiry'] > expiry:
                    result = browser.find_element(By.ID, 'result').text
                    expiry = key['expiry']
        print(result)


'''
Task 6:
Ваш основной инструмент для взаимодействия с веб-страницей.

Этапы миссии:

Идентификация Элемента: Первым делом необходимо найти элемент, с которым вы хотите взаимодействовать.
# Пример поиска элемента по ID
browser.find_element(By.ID, 'btn')
Получение Фокуса: Воспользуйтесь методом scrollIntoView для того, чтобы прокрутить страницу так, чтобы нужный элемент оказался в видимой области.
# Пример получения фокуса элемента
element = browser.find_element(By.CLASS_NAME, 'btn')
browser.execute_script("return arguments[0].scrollIntoView(true);", element)
Клик по Элементу: Теперь, когда элемент в фокусе, попробуйте снова выполнить клик.
Проверка Результата: Убедитесь, что ваше взаимодействие с элементом привело к желаемому результату(в теге с  <p id="result">788544</p> появляется уникальное для каждой кнопки число).
Суммирование:  Суммируйте все полученные числа.
Завершающий этап: Вставьте полученную сумму в поле ответов на Степике.
'''


def test_task_6():
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('--headless')
    with webdriver.Chrome(options=options_chrome) as browser:
        browser.get('https://parsinger.ru/scroll/4/index.html')
        elements = browser.find_elements(By.CLASS_NAME, 'btn')
        result = 0
        for element in elements:
            browser.execute_script("return arguments[0].scrollIntoView(true);", element)
            element.click()
            result += int(browser.find_element(By.ID, 'result').text)
        print(result)


'''
Task 7:
Задачи
Случайная Локация: Откройте указанный сайт с помощью Selenium. Здесь вас встретят 100 текстовых полей, и рядом с некоторыми из них будут чекбоксы. Главная загвоздка: чекбоксы и их состояние ("checked" или нет) определяются случайным образом.

Числовая Сборка: Пройдитесь по всем 100 текстовым полям и соберите числа только из тех, которые имеют рядом "checked" чекбоксы.

Особенности и Условности
Поля и чекбоксы могут загружаться в разных комбинациях, поэтому рассчитывать на конкретную последовательность или паттерн не стоит.

Чекбоксы могут быть в двух состояниях: checked (отмечены) и unchecked (не отмечены). Мы интересуемся только числами из полей с отмеченными чекбоксами.

Собранные числа необходимо суммировать и полученный результат вставить в поле ответа степик.
'''


def test_task_7():
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('--headless')
    with webdriver.Chrome(options=options_chrome) as browser:
        browser.get('https://parsinger.ru/selenium/5.5/3/1.html')
        elements = browser.find_elements(By.CLASS_NAME, 'parent')
        result = 0
        for element in elements:
            if element.find_element(By.CLASS_NAME, 'checkbox').is_selected():
                result += int(element.find_element(By.TAG_NAME, 'textarea').text)
        print(result)


'''
Task 8:
Задачи
Исследование Территории: Откройте веб-сайт с помощью Selenium. Проанализируйте поля, с которыми предстоит работать.

Миссия "Синхронизация": На странице находятся 100 текстовых полей: 50 серых и 50 синих. Ваша задача — перенести числа из серых полей в синие.

Проверка и Контроль: Нажмите на кнопку "Проверить". Если перенос чисел прошёл успешно, поля станут зелёными.

Получение Кода: Секретный код появится только в том случае, если все поля успешно стали зелёными. Секретный код нужно будет вставить в поле для ответа на степик.
'''


def test_task_8():
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('--headless')
    with webdriver.Chrome(options=options_chrome) as browser:
        browser.get('https://parsinger.ru/selenium/5.5/4/1.html')
        elements = browser.find_elements(By.CLASS_NAME, 'parent')
        for element in elements:
            number = element.find_element(By.CSS_SELECTOR, 'textarea[color="gray"]').text
            element.find_element(By.CSS_SELECTOR, 'textarea[color="gray"]').clear()
            element.find_element(By.CSS_SELECTOR, 'textarea[color="blue"]').send_keys(number)
            element.find_element(By.TAG_NAME, 'button').click()
        browser.find_element(By.ID, 'checkAll').click()
        print(browser.find_element(By.ID, 'congrats').text)


'''
Task 9:
Что вас ждёт на странице.
50 уникальных контейнеров (div), каждый с собственным случайным фоновым HEX цветом.
В каждом блоке присутствует выпадающий список с множеством HEX цветов.
Кнопки с разными цветами и уникальным атрибутом data-hex=.
Чек-боксы и текстовые поля, которые также хотят участвовать в этой великой красочной головоломке.


Что нужно сделать
Загрузка Страницы: Откройте страницу с помощью Selenium. 

Используйте эту страницу с двумя элементами для тренировки.

Коды Цветов: Получите цвет в формате HEX из каждого элемента <span>.

Выбор в Списке: В выпадающем списке в каждом контейнере найдите и выберите тот же HEX цвет что и у родительского контейнера.

Кнопочная Магия: Найдите и нажмите на кнопку, у которой атрибут data-hex совпадает с HEX цветом родительского контейнера.

Чек-Бокс Челлендж: Поставьте галочку в чек-боксе на странице.

Текстовое Поле: Вставьте в текстовое поле тот же HEX-цвет, который имеет фон родительского контейнера.

Подтверждение: Нажмите на кнопку "Проверить": если вставлен корректный HEX, то на кнопке появится "ОК".

Повторение: Повторите все эти шаги для каждого найденного на странице контейнера.

Финальный Шаг: После выполнения всех действий, нажмите на кнопку "Проверить все элементы", кнопка расположена в самом низу, появится alert если все условия соблюдены.

Секретный Код: Из алерт-окна получите числовой код и вставьте его в поле ответа степик.
'''


def test_task_9():
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('--headless')
    with webdriver.Chrome(options=options_chrome) as browser:
        browser.get('https://parsinger.ru/selenium/5.5/5/1.html')
        elements = browser.find_elements(By.XPATH, '//div[@id="main-container"]/div')
        for element in elements:
            color = element.find_element(By.XPATH, './/span').text
            select = Select(element.find_element(By.XPATH, './/select'))
            select.select_by_value(color)
            element.find_element(By.XPATH, f'.//button[@data-hex="{color}"]').click()
            element.find_element(By.XPATH, './/input[@type="checkbox"]').click()
            element.find_element(By.XPATH, './/input[@type="text"]').send_keys(color)
            element.find_element(By.XPATH, './/button[text()="Проверить"]').click()
        browser.find_element(By.XPATH, '//button[text()="Проверить все элементы"]').click()
        print(browser.switch_to.alert.text)


'''
Task 10:
Цель: Получить все секретные "cookies" с заданного веб-сайта и суммировать их числовые значения. Эти "cookies" могут хранить важную информацию, например, ключи для доступа к секретным данным. Ваши навыки веб-парсинга здесь будут более чем полезны.
 

Этапы миссии:

Вооружитесь браузером и пусть ваш код проникнет на сайт.
Поиск секретных cookies: Найдите все скрытые secret_cookie_, которые могут содержать важную информацию.


Дешифровка и анализ: Суммируйте числовые значения всех secret_cookie_. Это может быть частью шифра или ключом к следующему уровню.
Ввод ответа: Вставьте полученную сумму в поле ответа степик. Это ваш ключ к успешному завершению миссии.
'''


def test_task_10():
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('--headless')
    with webdriver.Chrome(options=options_chrome) as browser:
        browser.get('https://parsinger.ru/methods/3/index.html')
        cookies = browser.get_cookies()
        sum_cookies = 0
        for cookie in cookies:
            sum_cookies += int(cookie['value'])
        print(sum_cookies)


'''
Task 11:
Этапы миссии:

Переход на сайт: Используйте Selenium для того, чтобы перейти на целевой веб-сайт.

Загрузка данных: Загрузите 100 комплектов cookies (под спойлерм внизу степа), присланных хакерской группой. Каждый cookie принадлежит одному из хакеров противоборствующей группы.

# Пример добавления кукис
driver.add_cookie({'name': 'cookie_name', 'value': 'cookie_value'})
Обновление страницы: Используйте driver.refresh() для того, чтобы применить новые cookies.
# Обновление страницы
driver.refresh()
Анализ и Вербовка: Пройдитесь по всем кукам и определите самого молодого и перспективного хакера — того, кто (1)младше всех и (2)знает больше всего языков программирования.
Извлечение данных: После того, как вы определите, кто из хакеров наиболее перспективен, извлеките "value" из его cookie.
cookies = webdriver.get_cookies()
    for cookie in cookies:
        print(cookie['name']) # или cookie['value'] чтобы получить их значение
# Удаление всех кукис для чистого эксперимента
driver.delete_all_cookies()
Завершающий этап: Вставьте полученное значение cookie['value'] в поле для ответов на Степике.
'''


def test_task_11():
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('--headless')
    cookies_dict = [{'name': 'KXIYO4xMrWh', 'value': 'ibyAZPfXAsPqptPaNyL'},
                    {'name': '0OIJ4G4ZLzK', 'value': 'kJcPzQu5Jr8ELK'},
                    {'name': 'O1C4sd3RK5udnZ6P', 'value': '4mYYxbfgnIvuip2ry58EQ'},
                    {'name': 'AUZgaLJ4Y', 'value': 'FLSZvYrkf1E57YMUkdD'},
                    {'name': '9PWJc0VXVtnXNcS5Tf', 'value': 'YQ2G4RayBoXSEqEgA3oXRN3FAvAMT'},
                    {'name': 'pN2x6MDb', 'value': 'htbtD59XD3vCemHRCe9iUxV1smvXAIk5XOwuHnnmMB0'},
                    {'name': 'AsqpQd', 'value': 'uNFFRiqeRrj25MwJajG4AxeKvCxKbHUSbbvzb3C'},
                    {'name': '73PVEdwTk0txDp4L', 'value': 'DTniz3Fwj110H24dfZfd5JqqfEtN'},
                    {'name': 'jZ1MwGy5z0L8ZW00U', 'value': 'sspfahNvfeo3zHWAIW0jdp2A9LyDbIm0'},
                    {'name': 'aLRosjpBhYrZ0J69a', 'value': 'zcoXWv5L9Pz5kwGeyP5jlAQ'},
                    {'name': '9LPCTyKTNmvBcnZ', 'value': 'GWBjw1Gosk4IKxuh5J2eu0ikgowOaZwP8FOm1ekKeQIxJDIXBy'},
                    {'name': 'psH0h', 'value': 'wNAUmVlQwG6VK5TvDfryipzWeLXX46WDbXUd8yGrhrA3Hnc'},
                    {'name': 'BULl3P', 'value': 'wefA0ljyA82kYpV1OoOixtAIp6xjmiQlS9SLeN'},
                    {'name': '3bIJVJCylqgshRC9r1dH', 'value': '6Y6EZE5dttgx7rKzP881nAhRPE'},
                    {'name': 'dBDhCzi6VO0', 'value': 'LKMcpZ6bEJy5IY352OMViznSP5OMqS9IgZB0YMv'},
                    {'name': '6SGnnuoZ7v', 'value': '6asdYiIPBsMEdO0mQ9Jlq0mSMbJjfg'},
                    {'name': '4dfAVZ1qZwijwYMUj', 'value': '3TOxOPelSdN6cK273'},
                    {'name': 'RMOPZQILwFr3o637M', 'value': 'RZoaTFTdytqxB6sZhO4ebrhWlxjhMoQn8ZiObpdcGgH'},
                    {'name': '08cQ7E3qHOOMk4uy1fLz', 'value': 'YfYkz9boRjDHLTahMuZcAJPzbjwTlRt1iNZzGl'},
                    {'name': 'YT1NKf55egy', 'value': '3MSmfnklFY5TzvM8np4guMsJYtmdHmbyHiz3Vp6Rtk7r4GWhC'},
                    {'name': 'cTKnm0a3H2euL46Ibi', 'value': 'HCZ0KYkidXfFowGinPuWG19cT79gEJC'},
                    {'name': 'mvAz0P7Igjs2JY', 'value': '8O67zvSDHJx'},
                    {'name': 'TzWXbWMvDBcKTo', 'value': 'dzwNYZCg4jpxKtpCeumwq0DO2KtGWLIHpQLOrzmGbXMC8G'},
                    {'name': '1BMgyMHkzUemIEr', 'value': '08Sd1v8kQi6eB1FTs9qfjDkJ9UfKCLOFGtDgbOlu9v9iiuu'},
                    {'name': 'Jig5voy', 'value': 'Pi4OA6hY21TeHlHyPMaMFHgY0BZRcQ9V0nXg'},
                    {'name': '10wa7lhCoJXIzEYW5kQ', 'value': 'BFp4YeKWKVKXHTOesJLleaAelwYwPz51C95IYzd'},
                    {'name': 'BqXt5D', 'value': 'n99ZSFFhseCs7aVjU31pYSJxqMgFYGfreFZl9ixb2NNHRBp'},
                    {'name': 'GJunU5e1BEvfd', 'value': 'y5YFJ3hF9hG45G86MD9W9nRk61JMsh8rsmbFFrDoeJVUfyBvZ'},
                    {'name': 'itFJBn79wksvZ15lc2', 'value': 'nXpdqpt0Po84uOuSU'},
                    {'name': 'O5Q70eOB5ivJt5DZ', 'value': 'AZRr2ATREeF9HQR2opgF'},
                    {'name': '6jBEUxI0a7x790m', 'value': 'comi8Mx5ig95NAiSO8'},
                    {'name': 'KpVF7aIkav32LuqIDI', 'value': 'ik4furgLieyUawgJpttvHxWoXm2zO19'},
                    {'name': 'OTRFyN', 'value': 'vlzV7Z97sWcJStZgDJiRjzIf'},
                    {'name': 'hKLzMbgdIlUTAMYSEo', 'value': 'Tq2l0QJ3ekwxY3uaC8n2ln1nDMWhltFQm2TNaBefAAzk'},
                    {'name': 'GJKNrAvRn', 'value': 'dByJXuSsAIz3Rnqa9BvU11okpnSydEZnkaqMQu9RoE'},
                    {'name': 'AowB8Q3t74JHmXTGc1', 'value': '02JklRAtbsNNe'},
                    {'name': 'xPpvKmo03bGBYrmqw', 'value': '7bf4FgaLKoj6YvGq4huLT5r9eCflo70QhI9gAPkMIuj4Bg'},
                    {'name': '8UqFFBP3Dm0s6XM', 'value': 'kSZJPw6oTBwqG94q'},
                    {'name': 'WeeXL7bKNWIZZkgX', 'value': 'ap3DPbBYqlfEOZ6'},
                    {'name': 'fhdSevpxKUzledgGtbL4', 'value': 'v5I4A3PFOlN9zWPDkedlC2eLbMZ5cn3cf8'},
                    {'name': '3H6lO', 'value': 'jxc9994fPQBKpnyr8aZBDZlMAolnxXh'},
                    {'name': 'QVen8QnA1648g4Dm9p', 'value': 'RXNYpaUTJlD4xVIOm'},
                    {'name': '3PxMnD9w', 'value': 'JC74xNLEc5ujZge7OmXj5EWk3hwdm4OH8FgF60D6pFl'},
                    {'name': 'o8yY57CZSN', 'value': 'afO10rX663gaVttfSxeE70Gd22JKxwJAli7EhEdzkxxME'},
                    {'name': 'UpAdf46rvxXW', 'value': 'Ft2FEQV71gLnG'},
                    {'name': 'WRrpVIAkMKiZVxHt299', 'value': 'FC53hjqCGooNgV'},
                    {'name': 'XHViH149aRl5', 'value': 'YbozZeoGCt3gO1kRMoLExcfCotBz'},
                    {'name': 'yjNLzeR4k', 'value': 'Chd2mmuK7nxuVTi'},
                    {'name': '5M4RGm', 'value': 'tj3HWN5mVpz9zgIie2ac2KHKIeABaou'},
                    {'name': 'CcxIZZYgojDZpHnO9zJl', 'value': 'xLiql8yXUxULBG9w2snaMLI4FjSyX'},
                    {'name': 'NScrEjcTmwo639PQqki', 'value': 'eOSFemtdjyphiPubTAzTICUhgw92By'},
                    {'name': '9b5OpL5NrCpmtsE', 'value': 'VKdEIeX5ZNTghD6sq3qyjBHJaUuXfpQ7YnYb'},
                    {'name': 'uyBoiSTHTtxV8Wszttb', 'value': 'SHEEfVcj1jNv3V1oqeT2wfEbWKZ0uJ2ljwv'},
                    {'name': 'qR6AeEoEbQb1GYRj', 'value': 'mA66a177y8e6Nm7BlKBvpcUrM3fm6y4K'},
                    {'name': 'l0Y9gn8MNtC', 'value': 'M1L2OUmAisn1c6DNB9mJfTHRM9V3HuXUAEGG8Zx'},
                    {'name': 'L8m4GeWyECR', 'value': 'QuFfnWXebyrwwqXfVvAN2dbSisST8IgGyLggrVzTjaCeQ'},
                    {'name': 'GxJSMQh9aZjFdhgjaAj', 'value': 'phOonlKiMt0xLDtvoB52TbATS1Ggm4Pv5lztk5vTNkXVqp'},
                    {'name': 'GRE1eZ8D1bb', 'value': 'llpIP76V4S978YmQcfW'},
                    {'name': 'dooT1cyS41bIWEB9c', 'value': 'ORu004k9aFl9FdS77Iz'},
                    {'name': 'csjauyxnCpBySvkXTDzS', 'value': 'SJKqcIqWDbUJbxnHfD8jNJzYKb3Yp3TPIRDIpxCNB'},
                    {'name': 'Y6CgAqWN8', 'value': 'qu0g6xEm0iJeTKM8NfOZUxP0XQaCtUfiTWHtQJ5soU5cpZ'},
                    {'name': 'xxtL44KLbN60b5q', 'value': 'RSNFhhicL7pWpo3gvE3tJbHaIjU'},
                    {'name': 'KcvqC30', 'value': '58IlGI646RMaGMYtL5XYqxFq8UaMwjPDNFNApAuDpUI9tMoM4t'},
                    {'name': 'y761v6wZDo3V7O', 'value': '3i9iZjnZXdHlJxDz7ZrkPthYdI3PowS5yRomV0v8fR9WVco4'},
                    {'name': 'Ixr7AetyC', 'value': 'lYRaNZAnoNHc9UZIoXI9E'},
                    {'name': 'QIvvsr04T0JGVJE', 'value': 'tr6fE8moJI897w967QTmKojC730GdkKTUonevQbYsHQ71mi'},
                    {'name': 'CBTq9zQjJx', 'value': 'z7BuIeFufYeZysVnrglrDJk8KW8UBWYt62'},
                    {'name': '2ALhFQM7svECfgsSaiTa', 'value': 'VGMsulQVoobUe4m6w8dZGej8jFzSES3hzl9OG2csqpl'},
                    {'name': '7VQixJTzu2H', 'value': 'jPnLpldHTFNgPCH1RUlmRQx7N58P7CQHajLYvGxho'},
                    {'name': 'KdmUSh1SJH6M9', 'value': 'HPKIgmOBqq6Ln6QSPKedXuFpOoWhrOUzCxRMlcoJ2Gd0S7Hd'},
                    {'name': 't6B9gl6QeGEDl1LW', 'value': 'kGs0hk4Pmeb83dBbuHTSzIVNcY0G4iucq73lkCMwt6Akv4w'},
                    {'name': 'gcjmy3', 'value': 'QtB6duKOGc7eNc9MFwiOOaikXCYQg6dO4m66sJJxkRebKIKiR'},
                    {'name': '2oBZU9j', 'value': '2U80qbFDpRElKTshedtaZ42OzYG48OQckEt2Zy9D7T'},
                    {'name': 'g2tyy8erqS4E5pdSynCB', 'value': 'VN5zSYJpNHQC14FVl'},
                    {'name': 'lLhLcbED3XAgAPaMp', 'value': 'tBUVWsfSNg0Iv4TLPAmBRm2m2nrWh'},
                    {'name': 'iUfgKa7OX', 'value': 'GtyGoiA00RNiTgqvbXs78khbzQ7d0rh5xTk1aZK'},
                    {'name': 'WQGGXKzZXvRXLC0', 'value': 'itGXA2mVtchzcqstP39BvfBvwh'},
                    {'name': 'p37sYwX5mgtwXJl3yFBL', 'value': 'h20iY8XooVE'},
                    {'name': 'tubsOLf', 'value': 'YGlaF0EEJrT1c5Z2HBAWnc1Q3an3Ob'},
                    {'name': 'mg1Pr2NJJEnw2UkGFg', 'value': 'L48wovkYz32wa16iiswcgbA6JmyVoysUqjfm4i7'},
                    {'name': 'V55E3ui8KHXybSDSSnoc', 'value': '7rhA8PSMZFy1aC8CQXbitOxY0qdUkDOUWijijIvlHhtB0q1'},
                    {'name': 'AcWBQQy', 'value': 'zl1GXRHA3neBLCN8'},
                    {'name': 'PtvgV4eJ21CrPE3xeH9', 'value': '1tU9KvLdq2uRNRKtA'},
                    {'name': 'XjuSocgLwoMvFo8a', 'value': 'pvmx5A97Sad0U6d6i'},
                    {'name': 'mMpdmPLcZEAZDzNyA8a2', 'value': 'WG6CrZ3zXfxN84hJXUKJq0ZroYditsADYplxwhkgXkUcZ'},
                    {'name': 'tojhHp0ZlGrZ8Y3', 'value': 'fqpJvGkfQRT7ytNTU5KPum150MmcVR1nja0QIQRVEOPiNvT7Pg'},
                    {'name': 'LDHgCR5PNoqYdffU5', 'value': '7a0tCBgGzylPTGUStOuNXORrRWwy03Upm2CvJX'},
                    {'name': 'F4xcvPzuYYAvDrvDi', 'value': 'zQEpxlKpKprtwFbJyx0XYxFrlc8XP2RhRG'},
                    {'name': 'fmnoi', 'value': 'yB9333KC4bP4SHUF90Kj7OC9QXz22WAZ3xtZxLi9'},
                    {'name': 'TbGdmTkjcC52T7q', 'value': '2HCejTOfB98e30JMj3Pz9Ok9xLz5Y9lkaJaHoRF2vA5xq0i'},
                    {'name': 'tg3vMrNIZHs', 'value': '2XRV99ShR8yc0bCe0QOuC9xd0A'},
                    {'name': '8FaJo5TVO7TmoOI', 'value': 'bGYulAOS3ARzN3Rsyx9JJzu'},
                    {'name': 'YLBwBAUCJ05p5fx2', 'value': 'Z8lGSb7AnZKVwlIqKgRIafpIfTVufj'},
                    {'name': 'fpZCwfH', 'value': 'cqo4KOj8LSagd6VUhBrq6RJtUquwK7mJaDQsQb'},
                    {'name': 'zjUiv081bH', 'value': 'LSJtgc56ylEJGMd1AhE9QcXudC8g'},
                    {'name': 'yiWR1RtAnWH71I1', 'value': 'ruskXwdCQOfbfIgtKcetVb'},
                    {'name': 'KMKvYURaBlIEmtyX', 'value': 'NFIzhI600J5QYN'},
                    {'name': 'hbFS4sDwQh', 'value': 's4zWhushscPPDDFqT5tzPJqix0HMjjG'},
                    {'name': 'b9wAAVSyw4V2LQ', 'value': 'SDkldbPnf6NjLZSxWZV7CpCW'},
                    {'name': 'jFhFn0wPFRG', 'value': 'RYqOrD21ZN7aUeBXqISZ2afocnvvwd6hw3BXUj1wEm0mUO'}]
    with webdriver.Chrome(options=options_chrome) as browser:
        browser.get('https://parsinger.ru/selenium/5.6/1/index.html')
        criteria = {'name': '', 'age': 99, 'skillsList': 0}
        for cookie in cookies_dict:
            browser.delete_all_cookies()
            browser.add_cookie(cookie)
            browser.refresh()
            name = browser.find_element(By.XPATH, '//span[@id="name"]').text[6:]
            age = int(browser.find_element(By.XPATH, '//span[@id="age"]').text[5:])
            skillsList = len(browser.find_element(By.XPATH, '//ul[@id="skillsList"]').text.split())
            if age < criteria['age'] and skillsList > criteria['skillsList']:
                criteria['name'] = name
                criteria['age'] = age
                criteria['skillsList'] = skillsList
                criteria['cookie_value'] = cookie['value']
        print(criteria['cookie_value'])
