from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from attributes.attribute_product import AttributeProduct as product


class Product:

    def __init__(self, wd):
        self.wd = wd

    @property
    def wait(self):
        return WebDriverWait(self.wd, 10)

    def find_elements(self):
        """Find elements"""
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, product.PRICE)))
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, product.QUANTITY)))
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, product.IN_CART)))
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, product.TAG_DESCRIPTION)))
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, product.TAG_REVIEWS)))

    def select_product(self, element=product.MAC):
        """Selects product on Main Page"""
        try:
            self.wd.find_element_by_css_selector(element).click()
        except NoSuchElementException:
            print(f'Error: product {element} not found')

    def open_image(self):
        """Open image
        Return image element  and number of images
        """
        images = self.wd.find_elements_by_css_selector(product.IMAGE_ADDITIONAL)
        image = images[0]
        image.click()
        image = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, product.IMAGE_OPEN)))
        number = len(images)
        return image, number

    def switch_image(self, number):
        """Click next image"""
        for i in range(number):
            self.wd.find_element_by_css_selector(product.NEXT_IMAGE).click()
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, product.IMAGE_OPEN)))

    def close_image(self):
        """Close image"""
        self.wd.find_element_by_css_selector(product.IMAGE_CLOSE).click()

    def wait_staleness(self, image):
        """Waiting for an item to disappear"""
        self.wait.until(EC.staleness_of(image))

    def select_option(self):
        """If product have option, make a selection"""
        try:
            option = Select(self.wd.find_element_by_css_selector(product.OPTION226))
            option.select_by_index(1)
        except NoSuchElementException:
            print("Product don't have option")

    def add_to_cart(self):
        """ CLick button add product to cart"""
        try:
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, product.IN_CART))).click()
        except TimeoutException:
            print(f'Error: locator {product.IN_CART} not found')

    def get_price(self):
        """ Return product's price"""
        price = self.wd.find_element_by_css_selector(product.CONTENT)
        price = price.find_element_bycss_selector(product.PRICE)
        return price

    def get_products_name(self):
        """ Return product's name"""
        name = self.wd.find_element_by_css_selector(product.CONTENT)
        name = name.find_element_by_css_selector(product.NAME_PRODUCT).text
        return name

    def alert_success(self):
        """
        Find alert success
        Return text
        """
        alert_text = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, product.ALERT_SUCCESS)))
        alert_text = alert_text.text
        return alert_text[:-2]
