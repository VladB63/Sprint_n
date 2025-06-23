import allure
from data import DataPage
from pages.base_page import BasePage
from locators.locators import MainLocators



class MainPage(BasePage):

    @allure.step('Переход по урлу')
    def open_url(self):
        self.go_to_url(DataPage.STAND_PRAKTIK)


    @allure.step('Ввод одинакового адреса')
    def dubl_point_from(self, address):
        self.add_text_to_element(MainLocators.INPUT_FROM, address)
        self.add_text_to_element(MainLocators.INPUT_WHERE, address)


    @allure.step('Ввод точки Откуда/Куда')
    def point_from_where(self):
        self.add_text_to_element(MainLocators.INPUT_FROM, DataPage.POINT_ADDRESS_FROM)
        self.add_text_to_element(MainLocators.INPUT_WHERE, DataPage.POINT_ADDRESS_WHERE)


    @allure.step('Поиск первой точки на карте')
    def find_first_poit_in_card(self):
        return self.find_element_with_wait(MainLocators.WAYPOINT_FIRST)


    @allure.step('Поиск второй точки на карте')
    def find_second_poit_in_card(self):
        return self.find_element_with_wait(MainLocators.WAYPOINT_SECOND)


    @allure.step('Поиск модального инфо окна')
    def find_modal_info_window(self, locator):
        return self.find_element_with_wait(locator)


    @allure.step('Поиск блока выбора маршрута')
    def find_marshrut_block(self):
        return self.find_element_with_wait(MainLocators.MARSHRUT_BLOCK)


    @allure.step('Поиск поля в блоке выбора под тарифом')
    def find_field_selection(self, locator):
        return self.find_element_with_wait(locator)


    @allure.step('Получение текста стоимости авто')
    def giv_price_auto(self):
        return self.giv_text_element(MainLocators.PRICE_AUTO)


    @allure.step('Получение текста статуса и времени в пути')
    def giv_status_and_time_auto(self):
        return self.giv_text_element(MainLocators.STATUS_TIME_AUTO)


    @allure.step('Клик по виду маршрута Оптимальный')
    def click_optimal_button(self):
        self.click_to_element(MainLocators.OPTIMAL_BUTTON)


    @allure.step('Клик по виду маршрута Свой')
    def click_mine_button(self):
        self.click_to_element(MainLocators.MINE_BUTTON)


    @allure.step('Поиск активного таба маршрута Оптимальный')
    def find_active_tab_optimal(self):
        return self.find_element_with_wait(MainLocators.ACTIV_OPTIMAL_BUTTON)


    @allure.step('Поиск активного таба маршрута Свой')
    def find_active_tab_mine(self):
        return self.find_element_with_wait(MainLocators.ACTIV_MINE_BUTTON)


    @allure.step('Поиск активного таба типа транспорта')
    def find_active_tab_type(self):
        return self.find_element_with_wait(MainLocators.ACTIV_TYPE_BUTTON)


    @allure.step('Поиск кнопки Вызвать такси')
    def find_call_button(self):
        return self.find_click_element_with_wait(MainLocators.CALL_TAXI_BUTTON)


    @allure.step('Клик по кнопке Вызвать такси')
    def click_call_taxi_button(self):
        self.click_to_element(MainLocators.CALL_TAXI_BUTTON)


    @allure.step('Клик по кнопке Драйв')
    def click_drive_button(self):
        self.click_to_element(MainLocators.DRIVE_BUTTON)


    @allure.step('Поиск кнопки Забронировать')
    def find_booking_button(self):
        return self.find_click_element_with_wait(MainLocators.BOOKING_BUTTON)


    @allure.step('Получение списка тарифов')
    def get_tarif_list(self):
        tarifs = self.find_elements_with_wait(MainLocators.TARIF)
        tarif_list = [tarif.text for tarif in tarifs]
        return tarif_list


    @allure.step('Поиск активного тарифа')
    def find_active_tarif(self):
        return self.find_element_with_wait(MainLocators.ACTIV_TARIF)


    @allure.step('Клик по тарифу')
    def click_tarif_button(self, tarif):
        self.click_to_element(tarif)


    @allure.step('Клик по кнопке Столик для ноутбука')
    def click_laptop_table_button(self):
        self.click_to_element(MainLocators.LAPTOP_SLIDER)


    @allure.step('Клик по кнопке ввести номер и заказать')
    def click_order_button(self):
        self.click_to_element(MainLocators.ORDER_BUTTON)


    @allure.step('Клик по кнопке Требования к заказу')
    def click_details_button(self):
        self.find_element_with_wait(MainLocators.FIELD_REQUIREMENTS)
        self.click_to_element(MainLocators.FIELD_REQUIREMENTS)


    @allure.step('Наведение курсора на иконку информации')
    def navi_info_icon_tarif(self, info):
        self.hover_over_element(info)

    @allure.step('Цикл для поиска локаторов')
    def verify_elements_displayed(self, locators):
        for locator in locators:
            element = self.find_element_with_wait(locator)
            return  element