import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


# Прокрутка содержимого страницы -execute_script()

def test_scroll_page_1():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/scroll/1/')
        browser.execute_script("window.scrollBy(0,5000)")
        time.sleep(10)


def test_scroll_page_with_ten_iterations():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/scroll/1/')
        for i in range(10):
            browser.execute_script("window.scrollBy(0,5000)")
            time.sleep(2)


def test_get_value_height_page():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/scroll/1/')
        height = browser.execute_script(
            "return document.body.scrollHeight")  # вернёт значение высоты основного элемента на странице — body
        time.sleep(2)
        print(height)


'''
window.innerHeight - получение высоты видимой области

window.innerWidth — получение ширины видимой области

window.scrollTo(0, document.body.scrollHeight) - прокрутить страницу до самого низа
'''


def test_get_visual_height():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/scroll/1/')
        height = browser.execute_script("return window.innerHeight")
        print(height)


def test_scroll_to_footer_page():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/scroll/1/')
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)


# Прокрутка содержимого страницы с помощью класса Keys

'''
driver = ... # инициализация драйвера
ActionChains(driver).key_down(Keys.SHIFT).send_keys("abc").perform() # Нажатие клавиши (Key down)

ActionChains(driver).key_down(Keys.SHIFT).send_keys("a").key_up(Keys.SHIFT).send_keys("b").perform() # Отпускание клавиши (Key up)
'''


def test_example_with_scroll():
    with webdriver.Chrome() as browser:
        browser.get(r"https://parsinger.ru/selenium/5.7/3/index.html")

        list_input = []  # Инициализируем пустой список для хранения обработанных элементов ввода
        while True:  # Начинаем бесконечный цикл

            # Ищем все элементы input на веб-странице и добавляем их в список input_tags
            input_tags = [x for x in browser.find_elements(By.TAG_NAME, 'input')]

            # Обходим каждый элемент input в списке
            for tag_input in input_tags:
                # Проверяем, не обрабатывали ли мы уже этот элемент ранее
                if tag_input not in list_input:
                    tag_input.send_keys(Keys.DOWN)  # Отправляем клавишу "Вниз"
                    browser.execute_script("return arguments[0].scrollIntoView(true);", tag_input)
                    tag_input.click()  # Кликаем на элемент
                    time.sleep(.3)
                    list_input.append(tag_input)  # Добавляем элемент в список обработанных элементов


# ActionChains(driver)(Цепочка действий)

'''
ActionChains(): Это способ автоматизации низкоуровневых взаимодействий, таких как движения мыши, действия с кнопками мыши, нажатие клавиш и взаимодействие с контекстным меню. 

ActionChains — класс, предназначенный для автоматизации сложных последовательностей действий пользователя.

Использование ActionChains для выполнения последовательности действий

actions = ActionChains(driver) # Создаём экземпляр класса ActionChains
actions.move_to_element(menu)  # Переместить курсор на элемент меню
actions.click(submenu)         # Кликнуть по подменю
actions.perform()              # Выполнить накопленные действия
'''


def test_with_action_chain():
    # Инициализация драйвера
    driver = webdriver.Chrome()

    # Открыть веб-страницу (замените URL на ваш адрес)
    driver.get("https://parsinger.ru/selenium/5.7/2/index.html")

    # Найти элемент на странице с использованием локатора By
    draggable = driver.find_element(By.ID, "draggable")

    # Использование ActionChains для выполнения перетаскивания элемента
    actions = ActionChains(driver)

    # 1. Переместить блок влево на 100px
    actions.drag_and_drop_by_offset(draggable, -100, 0).perform()

    # 2. Переместить блок вниз на 100px
    actions.drag_and_drop_by_offset(draggable, 0, 100).perform()

    # 3. Переместить блок вправо на 100px
    actions.drag_and_drop_by_offset(draggable, 100, 0).perform()

    # 4. Переместить блок вверх на 100px
    actions.drag_and_drop_by_offset(draggable, 0, -100).perform()

    # Закрыть браузер после завершения
    driver.quit()


'''
Методы ActionChains(driver)
actions = ActionChains(driver) # Создаём экземпляр класса ActionChains
element = driver.find_element(By.ID, "draggable") # Находим необходимый элемент/тег
 

1. action.perform(self) — Метод используется для выполнения всех сохраненных операций в экземпляре действия класса ActionChains. Запускает всю цепочку действий. 

2. action.click(element) — Кликает по элементу.

3. action.click_and_hold(element) — Удерживает левую кнопку мыши на элементе.

# Использование ActionChains для удержания левой кнопки мыши на элементе
actions = ActionChains(driver)
actions.click_and_hold(element_to_hold).perform()
 
4. action.context_click(element) — Используется для выполнения контекстного щелчка (щелчка правой кнопкой мыши) по элементу.

5. action.drag_and_drop(source, target) — Удерживает левую кнопку мыши на исходном элементе, затем перемещается к целевому элементу и отпускает кнопку мыши. 

# Найти исходный и целевой элементы на странице с использованием локаторов By
source = driver.find_element(By.ID, "source_element_id")
target = driver.find_element(By.ID, "target_element_id")

# Использование ActionChains для выполнения перетаскивания элемента
actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()

- source: Это исходный элемент, который вы хотите перетащить. source представляет собой тег, который вы хотите "взять" или начать перетаскивание. Обычно это элемент, который вы хотите переместить на другое место на веб-странице.
- target: Это целевой элемент, на который или к которому вы хотите перетащить исходный элемент. target представляет собой тег, на который или к которому вы хотите "отпустить" или завершить перетаскивание исходного элемента. Это место назначения, куда вы хотите переместить исходный элемент на веб-странице.

6. action.release(self, on_element=None)  — Метод release используется для отпускания удерживаемой кнопки мыши на элементе.

- self: Относится к текущему экземпляру объекта ActionChains, с которым вы работаете.
- on_element=None: Это параметр, который представляет собой элемент, на котором вы хотите отпустить кнопку мыши. Если этот параметр не указан (по умолчанию None), кнопка мыши будет отпущена на текущем положении курсора. Если вы укажете конкретный элемент в качестве on_element, кнопка мыши будет отпущена на этом элементе.

7. action.drag_and_drop_by_offset(source, xoffset, yoffset)  — Удерживает левую кнопку мыши на исходном элементе, затем перемещается к заданному смещению и отпускает кнопку мыши.

# Использование ActionChains для выполнения перетаскивания элемента на заданное смещение
actions = ActionChains(driver)
actions.drag_and_drop_by_offset(source_element, 50, 100).perform()  # Перемещает элемент на 50px вправо и 100px вниз

- source: Элемент для мыши.
- xoffset: X смещение для перехода.
- yoffset: Y смещение для перехода.
 
8. action.key_down(value, element) — Отправляет только нажатие клавиши, не отпуская ее. Следует использовать только с клавишами-модификаторами (Control, Alt и Shift).

# Использование ActionChains для удержания клавиш
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL, element) \
       .key_down(Keys.ALT) \
       .key_down(Keys.SHIFT) \
       .key_down('T') \
       .perform()
- value: Параметр представляет собой значение клавиши, которую вы хотите нажать. value может быть любой клавишей на клавиатуре, любыми клавишами (A, B, C и т. д.). Значения для этих клавиш обычно определены в классе Keys в Selenium. Рассматривали в этом степе;
- element: Параметр представляет собой элемент на веб-странице, к которому вы хотите отправить команду нажатия клавиши. Если этот параметр указан, клавиша будет "нажата" на этом конкретном элементе.

8. action.key_up(value, element)  — Метод используется для отпускания нажатой клавиши с помощью метода key_down.

# После выполнения необходимых действий, не забудьте отпустить клавиши
actions.key_up(Keys.CONTROL) \
       .key_up(Keys.ALT) \
       .key_up(Keys.SHIFT) \
       .key_up('T') \
       .perform()
       
- value: параметр представляет собой значение клавиши, которую вы хотите отпустить. В контексте функции key_up, value обычно представляет собой константу из класса Keys, которая соответствует определенной клавише на клавиатуре. Например, Keys.CONTROL, Keys.ALT или Keys.SHIFT.
- element:параметр, который представляет собой элемент, на котором вы хотите выполнить действие отпускания клавиши. Если этот параметр указан, клавиша будет отпущена на указанном элементе. Если этот параметр не указан, клавиша будет отпущена на текущем элементе в фокусе.

9. action.move_by_offset(xoffset, yoffset)  — Позволяет перемещать курсор мыши на определенное расстояние от его текущего положения на экране. Это особенно полезно, когда вы хотите выполнить точное перемещение курсора без необходимости ссылаться на конкретный элемент на веб-странице.

# Использование move_by_offset для перемещения курсора мыши на 50px вправо и 100px вниз
actions.move_by_offset(50, 100).perform()

- xoffset: Горизонтальное смещение, на которое вы хотите переместить курсор мыши относительно его текущего положения. Значение может быть положительным (для перемещения вправо) или отрицательным (для перемещения влево).
- yoffset: Вертикальное смещение, на которое вы хотите переместить курсор мыши относительно его текущего положения. Значение может быть положительным (для перемещения вниз) или отрицательным (для перемещения вверх).

10. action.move_to_element(to_element)  — Метод используется для перемещения мыши в середину элемента.

# Найти элемент на странице, к которому вы хотите переместить курсор
menu_element = driver.find_element(By.ID, "menu_item")

# Использование ActionChains для перемещения курсора к элементу
actions = ActionChains(driver)
actions.move_to_element(menu_element).perform()

- to_element: Элемент, к которому вы хотите переместить курсор мыши. В контексте функции, to_element должен быть объектом WebElement, который вы хотите указать или на который хотите навести курсор.

11. action.move_to_element_with_offset(to_element, xoffset, yoffset) — Метод используется для перемещения мыши на смещение указанного элемента. Смещения относятся к верхнему левому углу элемента.

# Переместить курсор мыши на 50px вправо и 30px вниз от верхнего левого угла элемента element_to_hover
actions.move_to_element_with_offset(element_to_hover, 50, 30).perform()

- to_element: WebElement, к которому нужно перейти.
- xoffset: X смещение для перехода.
- yoffset: Y смещение для перехода.
 
12. action.pause(seconds) — Метод паузы используется для приостановки всех входящих данных на указанное время в секундах. Метод паузы очень важен и полезен в случае выполнения какой-либо команды, для загрузки которой требуется какой-либо JavaScript, или в подобной ситуации, когда между двумя операциями есть временной промежуток.

13. action.send_keys(Keys.DOWN) — метод используется для отправки ключей текущему элементу в фокусе;

- Keys.DOWN:  - значения  клавиши определены в классе Keys. 

14. action.send_keys_to_element(element, *keys_to_send) — Метод используется для отправки нажатия клавиша текущему элементу в фокусе.

# Найти элемент на странице с использованием локатора By
input_element = driver.find_element(By.ID, "inputField")

# Использование ActionChains для отправки нажатия клавиш элементу
actions = ActionChains(driver)
actions.send_keys_to_element(input_element, "Hello", Keys.SPACE, "World!").perform()

- element: Элемент, к которому вы хотите отправить нажатия клавиш. Это должен быть объект WebElement, который вы уже нашли на веб-странице.
- *keys_to_send: Последовательность клавиш, которые вы хотите отправить к указанному элементу. Вы можете отправить одну или несколько клавиш, используя этот параметр. Клавиши могут быть представлены строками (например, "Hello") или константами из класса Keys (например, Keys.ENTER или Keys.TAB). Звездочка (*) перед keys_to_send в сигнатуре функции указывает на то, что метод может принимать переменное количество аргументов, переданных как отдельные параметры.

15. action.scroll(x, y, delta_x, delta_y, duration, origin=element)  —  Выполняет скроллинг на элементе, где установлен курсор. Очень полезный скроллинг, позволяет прицельно скролить окна маленьких размеров;

- x: Координата по горизонтали, где установлен курсор. Она определяет начальное положение курсора по оси X перед началом скроллинга.
- y: Координата по вертикали, где установлен курсор. Она определяет начальное положение курсора по оси Y перед началом скроллинга.
- delta_x: Расстояние, на которое курсор будет прокручиваться по горизонтали (оси X). Положительное значение прокрутит содержимое вправо, отрицательное — влево.
- delta_y: Расстояние, на которое курсор будет прокручиваться по вертикали (оси Y). Положительное значение прокрутит содержимое вниз, отрицательное — вверх.
- duration: Время (в секундах), которое будет затрачено на выполнение скроллинга. Это позволяет контролировать скорость прокрутки.
- origin: Элемент, относительно которого будет выполняться скроллинг. Если этот параметр не указан, скроллинг будет выполняться относительно текущего положения курсора. Если указан конкретный элемент, скроллинг будет выполняться относительно этого элемента.

16. action.reset_actions(self) — Метод очищает действия, которые уже сохранены локально и в ActionChains. Это один из наиболее часто используемых методов, так как после какой-либо операции необходимо сбросить экземпляр ActionChains для выполнения следующей операции.

17. action.scroll_by_amount(delta_x, delta_y) — Метод прокручивает на заданное количество, начало координат находится в верхнем левом углу области просмотра.

# Использование ActionChains для прокрутки на заданное количество
actions = ActionChains(driver)
actions.scroll_by_amount(delta_x=50, delta_y=100).perform()  # Прокрутка на 50 пикселей вправо и 100 пикселей вниз

- delta_x: Cмещение по горизонтали. Положительное значение будет прокручивать содержимое вправо, а отрицательное значение — влево.
- delta_y: Cмещение по вертикали. Положительное значение будет прокручивать содержимое вниз, а отрицательное значение — вверх.

18. action.scroll_from_origin(scroll_origin, delta_x, delta_y) — Выполняет прокрутку на указанное расстояние на основе исходного положения. 

# Найти элемент на странице с использованием локатора By
element_to_scroll = driver.find_element(By.ID, "someElement")

# Использование ActionChains для выполнения прокрутки относительно элемента
actions = ActionChains(driver)
actions.scroll_from_origin(element_to_scroll 0, 100).perform()  # Прокрутка вниз на 100 пикселей относительно элемента

- scroll_origin: Место, откуда начинается прокрутка (область просмотра или центр элемента) плюс предоставленные смещения.
- delta_x: Расстояние по оси X для прокрутки с помощью колеса. Отрицательное значение прокручивает влево.
- delta_y: Расстояние по оси Y для прокрутки с помощью колеса. Отрицательное значение прокручивает вверх.

19. action.scroll_to_element(element) — Метод предназначен для автоматического прокручивания страницы к указанному элементу.

# Найти элемент на странице
element = driver.find_element(By.ID, "someElement")

# Использование ActionChains для прокрутки к элементу
actions = ActionChains(driver)
actions.scroll_to_element(element).perform()

20. scroll_by_amount(delta_x, delta_y) — позволяет скролить любое окно на заданное количество пикселей
 
- delta_x: расстояние по оси X для прокрутки с помощью колеса. Отрицательное значение прокручивается влево.   
- delta_y: расстояние по оси Y для прокрутки с помощью колеса. Отрицательное значение прокручивается вверх.
'''

'''
Task 1:
Цель
Инициализация: Откройте заданный веб-сайт http://parsinger.ru/scroll/2/index.html с помощью Selenium.

Обнаружение чекбоксов: На сайте будет 100 чекбоксов. Если кликнуть на чекбокс, может появится число в теге span 

<span id="result1">954</span>


Вычисление: Соберите все эти числа и сложите их. 

Отправка ответа: Введите сумму всех чисел, в поле ответа на Stepik.
'''


def test_task_1():
    with webdriver.Chrome() as browser:
        browser.get('http://parsinger.ru/scroll/2/index.html')
        numbers = browser.find_elements(By.XPATH, '//span')
        input_tags = browser.find_elements(By.TAG_NAME, 'input')
        lst = []
        step = 0

        for num in numbers:
            input_tags[step].send_keys(Keys.DOWN)  # Отправляем клавишу "Вниз"
            browser.execute_script("return arguments[0].scrollIntoView(true);", input_tags[step])
            input_tags[step].click()
            step += 1
            if num.text != '':
                lst.append(int(num.text))
        print(sum(lst))


'''
Task 2:
Цель
Инициализация: Используя Selenium, откройте заданный веб-сайт https://parsinger.ru/infiniti_scroll_1.

Скроллинг: На сайте имеется список из 100 элементов, который расширяется при скроллинге (infinity scroll).

Сбор данных: Скрольте по интерактивным элементам, чтобы раскрыть все 100 элементов списка. Используйте Keys.DOWN или методы ActionChains(driver).

Агрегация: Извлеките все числовые значения из этих элементов и сложите их.

Отправка ответа: Вставьте собранную сумму чисел в предназначенное поле на сайте.
'''


def test_task_2():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/infiniti_scroll_1')
        div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
        for x in range(10):
            ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()
        print(sum(int(number.text) for number in browser.find_elements(By.TAG_NAME, 'span') if number.text))


'''
Task 3:
Задача
Инициализация: Откройте заданный веб-сайт https://parsinger.ru/infiniti_scroll_2 с помощью Selenium.

Техника скроллинга: Сайт содержит список из 100 элементов, которые появляются только при скроллинге. Стандартные элементы типа чекбоксов или другие элементы для "зацепления" тут отсутствуют.

Навигация: Прокрутите страницу до самого низа, используя ActionChains.

Сбор информации: Извлеките все числовые значения из появившихся элементов и сложите их.

Отправка результата: Вставьте полученную сумму в соответствующее поле для ответа на степик.
'''


def test_task_3():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/infiniti_scroll_2')
        div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
        for x in range(10):
            ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()
        element = browser.find_elements(By.XPATH, '//p')
        amount = []
        for val in element:
            if (val.text).isdigit():
                amount.append(int(val.text))
        print(sum(amount))


'''
Task 4:
Задача
Инициализация: Откройте заданный веб-сайт https://parsinger.ru/infiniti_scroll_3 с помощью Selenium.

Множественная навигация: На сайте есть 5 разных окон, в каждом из которых подгружается по 100 элементов при скроллинге.

Техника скроллинга: Для каждого окна прокрутите страницу до самого низа. Здесь можно использовать ActionChains для эффективного скроллинга.

Сбор информации: Из каждого окна извлеките все числовые значения и сложите их. Суммируйте данные из всех окон.

Отправка результата: Вставьте полученную сумму в соответствующее поле для ответа на сайте.
'''


def test_task_4():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/infiniti_scroll_3')
        for q in range(5):
            div = browser.find_element(By.XPATH, f'//*[@class="scroll-container_{q + 1}"]/div')

            for x in range(10):
                ActionChains(browser).move_to_element(div).scroll_by_amount(0, 500).perform()
            amount = browser.find_elements(By.XPATH, '//span')
            amount_lst = []

            for g in amount:
                if (g.text).isdigit():
                    amount_lst.append(int(g.text))
        print(sum(amount_lst))


'''
Task 5:
Задачи:
Стартовая Позиция: Запустите Selenium и откройте данный веб-сайт https://parsinger.ru/selenium/5.7/1/index.html. Убедитесь, что ваша станция готова к операции.

Сбор Урана: Пройдитесь по каждому кусочку урана на странице и кликните по нему. Это поможет нам вернуть его обратно на корабль.

#Подсказка
driver.execute_script("return arguments[0].scrollIntoView(true);", button)
Получение Секретного Кода: Как только в открытом космосе не останется ни одного кусочка урана, команда пришлёт вам в alert-окне секретный код.

#Подсказка
alert_text = alert.text
Финальный Этап: Вставьте полученный секретный код в необходимое поле для завершения операции.
'''


def test_task_5():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/5.7/1/index.html')
        element = browser.find_elements(By.CLASS_NAME, 'button-container')
        for x in element:
            browser.find_element(By.CLASS_NAME, 'clickMe').click()
        time.sleep(3)
        alert_text = browser.switch_to.alert.text
        print(alert_text)


'''
Task 6:
Задача
Откройте сайт https://parsinger.ru/selenium/5.7/5/index.html с помощью Selenium.
Найдите все четыре кнопки на странице.
Определите значение value каждой кнопки. Это время, которое необходимо удерживать кнопку.
Как только все кнопки станут зелёными, вы получите сообщение в alert. Скопируйте это сообщение.
Вставьте полученное сообщение в поле ответа на Stepik.
 
Подсказка:
Вам потребуется использовать методы вроде ActionChains для удержания кнопки
# Пример
actions.click_and_hold(button).pause(hold_time).release(button).perform()
'''


def test_task_6():
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/5.7/5/index.html')
        buttons = browser.find_elements(By.CLASS_NAME, 'timer_button')
        for sec in buttons:
            ActionChains(browser).click_and_hold(sec).pause(float(sec.text)).release(sec).perform()
        print(browser.switch_to.alert.text)