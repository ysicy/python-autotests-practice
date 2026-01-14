from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    DEFAULT_WAIT = 15

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_WAIT)
        self.actions = ActionChains(driver)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def fill(self, by: By, value: str, *, text: str):
        el = self.wait.until(expected_conditions.element_to_be_clickable((by, value)))
        el.clear()
        el.send_keys(text)

    def click(self, by: By, value: str):
        self.wait.until(expected_conditions.element_to_be_clickable((by, value))).click()

    def text(self, by: By, value: str,) -> str:
        return self.wait.until(expected_conditions.visibility_of_element_located((by, value))).text

    def is_visible(self, by: By, value: str) -> bool:
        return bool(self.wait.until(expected_conditions.visibility_of_element_located((by, value))))

    def is_invisible(self, by: By, value: str, timeout: int = None) -> bool:
        """Проверяет, что элемент невидим или отсутствует на странице"""
        wait_time = timeout if timeout is not None else self.DEFAULT_WAIT
        wait = WebDriverWait(self.driver, wait_time)
        return bool(wait.until(expected_conditions.invisibility_of_element_located((by, value))))

    def wait_until_visible(self, by: By, value: str, timeout: int = None):
        wait_time = timeout if timeout is not None else 3
        wait = WebDriverWait(self.driver, wait_time)
        wait.until(expected_conditions.visibility_of_any_elements_located((by, value)))

    def wait_until_invisible(self, by: By, value: str, timeout: int = None):
        wait_time = timeout if timeout is not None else 3
        wait = WebDriverWait(self.driver, wait_time)
        wait.until(expected_conditions.invisibility_of_element_located((by, value)))