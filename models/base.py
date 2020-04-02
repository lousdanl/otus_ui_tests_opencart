import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select

TIME_EXPLICIT_WAIT = 10


class Base:
    def __init__(self, wd):
        self.wd = wd

    @classmethod
    def _selector_method(cls, selector: tuple):
        """Выбор селектора"""
        by = None
        if selector[0] == 'css':
            by = By.CSS_SELECTOR
        elif selector[0] == 'xpath':
            by = By.XPATH
        elif selector[0] == 'text':
            by = By.LINK_TEXT
        return by, selector[1]

    def _element(self, selector: tuple):
        """
        Общий метод для поиска элемента
        """
        by, locator = self._selector_method(selector)
        element = self.wd.find_element(by, locator)
        return element

    def _elements(self, selector: tuple):
        """
        Общий метод для поиска элементов
        """
        by, locator = self._selector_method(selector)
        elements = self.wd.find_elements(by, locator)
        return elements

    def _element_method(self, selector):
        """Если передан кортеж, совершается поиск элемента, вовзращается элемент
         В другом случае передан элемент, вовзращает его"""
        if isinstance(selector, tuple):
            element = self._element(selector)
        else:
            element = selector
        return element

    def _elements_method(self, selector):
        """Если передан кортеж, совершается поиск элемента, вовзращается элемент
         В другом случае передан элемент, вовзращает его"""
        if isinstance(selector, tuple):
            element = self._elements(selector)
        else:
            element = selector
        return element

    def _in_element(self, parent_element, child_element):
        """Поиск внутри родительского элемента"""
        by, locator = self._selector_method(child_element)
        element = self._element_method(parent_element)
        return element.find_element(by, locator)

    def _in_elements(self, parent_element, child_element):
        """Ищем внутри родительского элемента"""
        by, locator = self._selector_method(child_element)
        element = self._element_method(parent_element)
        return element.find_elements(by, locator)

    def _click(self, selector):
        """Метод для работы с кнопками"""
        element = self._element_method(selector)
        ActionChains(self.wd).move_to_element(element).click().perform()

    def _input(self, selector, value):
        """Внесение данных"""
        element = self._elements(selector)[0]
        element.clear()
        element.send_keys(value)

    def _wait(self, method, selector):
        """Ожидание элемента """
        wait = WebDriverWait(self.wd, TIME_EXPLICIT_WAIT)
        if isinstance(selector, tuple):
            by, locator = self._selector_method(selector)
            return wait.until(method((by, locator)))
        else:
            return wait.until(method(selector))

    def _wait_element(self, selector):
        """Ожидание, элемент виден"""
        return self._wait(EC.visibility_of_element_located, selector)

    def wait_staleness_of(self, selector):
        """Ожидание, элемент пропал"""
        return self._wait(EC.staleness_of, selector)

    def _wait_clickable(self, selector):
        """Ожидание, элемент кликабельный"""
        return self._wait(EC.element_to_be_clickable, selector)

    def _wait_click(self, selector):
        """Ожидание элемента, нажатие"""
        element = self._wait_element(selector)
        self._click(element)

    def menu_select(self, select, value):
        """Селект по значению"""
        menu = Select(self._element(select))
        menu.select_by_value(value)

    def menu_select_by_index(self, select, value):
        """Селект по индексу"""
        menu = Select(self._element(select))
        menu.select_by_index(value)

    @classmethod
    def add_id(cls, selector, product_id):
        """Добавление к селектору элемента ид"""
        selector = list(selector)
        selector = selector[0], selector[1] % product_id
        return tuple(selector)

    def remove_attribute(self, element_id, name_attribute):
        self.wd.execute_script('document.getElementById("%s").removeAttribute("%s")' % (element_id, name_attribute))
        time.sleep(0.5)

    def _click_b(self, selector):
        self.wd.execute_script(f"$({selector}).click();")

    def add_element_to_body(self, element):
        self.wd.execute_script(f'$(\'body\').prepend(\'{element}\')')
