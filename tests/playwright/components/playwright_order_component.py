from playwright.sync_api import Locator


class OrderComponent:
    def __init__(self, element: Locator):
        self.element = element  # Корневой элемент компонента

    @property
    def id(self) -> str:
        # Поиск внутри компонента относительно корневого элемента
        element = self.element.locator("h6")
        return element.text_content().replace("Заказ №", "").strip()

    @property
    def status(self) -> str:
        # CSS селектор для поиска статуса
        element = self.element.locator("span.MuiChip-label")
        return element.text_content()

    @property
    def comment(self) -> str:
        # XPath для поиска комментария
        element = self.element.locator("xpath=.//p[contains(text(),'Комментарий:')]")
        return element.text_content().replace("Комментарий: ", "").strip()

    def delete(self) -> None:
        # Поиск кнопки удаления по data-testid
        self.element.locator("[data-testid^='orders-delete-btn-']").click()