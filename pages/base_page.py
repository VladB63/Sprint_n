import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    @allure.step('Переход по урлу')
    def go_to_url(self, url):
        self.driver.get(url)


    @allure.step('Поиск элемента')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)



    @allure.step('Поиск элемента')
    def find_element_in_modal_window(self, locator):
        WebDriverWait(self.driver, 40).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)


    @allure.step('Поиск элементов')
    def find_elements_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)


    @allure.step('Поиск кликабельного элемента')
    def find_click_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)


    @allure.step('Ввод текста в поле')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)


    @allure.step('Получить текст элемента')
    def giv_text_element(self, locator):
        return self.find_element_with_wait(locator).text


    @allure.step('Клик по элементу с ожиданием')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()


    @allure.step('Наведение курсора на элемент')
    def hover_over_element(self, locator):
        element = self.find_element_with_wait(locator)
        action = ActionChains(self.driver).move_to_element(element).click()
        action.perform()

