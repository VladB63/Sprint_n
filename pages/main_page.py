import allure
from data import DataPage
from pages.base_page import BasePage
from locators.locators import MainLoc



class MainPage(BasePage):

    @allure.step('Переход по урлу')
    def open_url(self):
        self.go_to_url(DataPage.STAND_PRAKTIK)


    @allure.step('Ввод одинакового адреса')
    def dubl_point_from(self, address):
        self.add_text_to_element(MainLoc.INPUT_FROM, address)
        self.add_text_to_element(MainLoc.INPUT_WHERE, address)


    @allure.step('Ввод точки Откуда/Куда')
    def point_from_where(self):
        self.add_text_to_element(MainLoc.INPUT_FROM, DataPage.POINT_ADDRESS_FROM)
        self.add_text_to_element(MainLoc.INPUT_WHERE, DataPage.POINT_ADDRESS_WHERE)


    @allure.step('Поиск первой точки на карте')
    def find_first_poit_in_card(self):
        return self.find_element_with_wait(MainLoc.WAYPOINT_FIRST)


    @allure.step('Поиск второй точки на карте')
    def find_second_poit_in_card(self):
        return self.find_element_with_wait(MainLoc.WAYPOINT_SECOND)


    @allure.step('Поиск модального инфо окна')
    def find_modal_info_window(self, locator):
        return self.find_element_with_wait(locator)


    @allure.step('Поиск модального окна Заказа')
    def find_order_modal_window(self):
        return self.find_element_with_wait(MainLoc.ORDER_MODAL_WINDOW)


    @allure.step('Поиск номера авто в модальном окне')
    def find_car_number_window(self):
        return self.find_element_in_modal_window(MainLoc.CAR_NUMBER)


    @allure.step('Поиск блока выбора маршрута')
    def find_marshrut_block(self):
        return self.find_element_with_wait(MainLoc.MARSHRUT_BLOCK)


    @allure.step('Поиск поля в блоке выбора под тарифом')
    def find_field_selection(self, locator):
        return self.find_element_with_wait(locator)


    @allure.step('Поиск активного таба маршрута Оптимальный')
    def find_active_tab_optimal(self):
        return self.find_element_with_wait(MainLoc.ACTIV_OPTIMAL_BUTTON)


    @allure.step('Поиск активного таба маршрута Свой')
    def find_active_tab_mine(self):
        return self.find_element_with_wait(MainLoc.ACTIV_MINE_BUTTON)


    @allure.step('Поиск активного таба типа транспорта')
    def find_active_tab_type(self):
        return self.find_element_with_wait(MainLoc.ACTIV_TYPE_BUTTON)


    @allure.step('Поиск кнопки Вызвать такси')
    def find_call_button(self):
        return self.find_click_element_with_wait(MainLoc.CALL_TAXI_BUTTON)


    @allure.step('Поиск кнопки Забронировать')
    def find_booking_button(self):
        return self.find_click_element_with_wait(MainLoc.BOOKING_BUTTON)


    @allure.step('Поиск активного тарифа')
    def find_active_tarif(self):
        return self.find_element_with_wait(MainLoc.ACTIV_TARIF)


    @allure.step('Клик по виду маршрута Оптимальный')
    def click_optimal_button(self):
        self.click_to_element(MainLoc.OPTIMAL_BUTTON)


    @allure.step('Клик по виду маршрута Свой')
    def click_mine_button(self):
        self.click_to_element(MainLoc.MINE_BUTTON)


    @allure.step('Клик по кнопке Вызвать такси')
    def click_call_taxi_button(self):
        self.click_to_element(MainLoc.CALL_TAXI_BUTTON)


    @allure.step('Клик по кнопке Драйв')
    def click_drive_button(self):
        self.click_to_element(MainLoc.DRIVE_BUTTON)

    @allure.step('Клик по тарифу')
    def click_tarif_button(self, tarif):
        self.click_to_element(tarif)


    @allure.step('Клик по кнопке Столик для ноутбука')
    def click_laptop_table_button(self):
        self.click_to_element(MainLoc.LAPTOP_SLIDER)


    @allure.step('Клик по кнопке Отмена')
    def click_cancel_button(self):
        self.click_to_element(MainLoc.CANCEL_BUTTON)


    @allure.step('Клик по кнопке ввести номер и заказать')
    def click_order_button(self):
        self.click_to_element(MainLoc.ORDER_BUTTON)


    @allure.step('Клик по кнопке Детали')
    def click_details_button(self):
        self.click_to_element(MainLoc.DETAIL_BUTTON)


    @allure.step('Клик по кнопке Требования к заказу')
    def click_requirements_button(self):
        self.find_element_with_wait(MainLoc.FIELD_REQUIREMENTS)
        self.click_to_element(MainLoc.FIELD_REQUIREMENTS)


    @allure.step('Получение текста стоимости авто')
    def giv_price_auto(self):
        return self.giv_text_element(MainLoc.PRICE_AUTO)


    @allure.step('Получение текста статуса и времени в пути')
    def giv_status_and_time_auto(self):
        return self.giv_text_element(MainLoc.STATUS_TIME_AUTO)


    @allure.step('Получение названия Тарифа и его описания из Инфо окна')
    def giv_name_and_description_tarif(self, loc_name, loc_descrip):
        name = self.giv_text_element(loc_name)
        description = self.giv_text_element(loc_descrip)
        return f'{name} - {description}'


    @allure.step('Получение списка тарифов')
    def get_tarif_list(self):
        tarifs = self.find_elements_with_wait(MainLoc.TARIF)
        tarif_list = [tarif.text for tarif in tarifs]
        return tarif_list


    @allure.step('Получение стоимости поездки из деталей')
    def giv_price_trip(self):
        element = self.find_element_with_wait(MainLoc.PRICE_TRIP).text
        trip = element.split()
        sum_price = trip[2]
        price = sum_price.replace('₽', '').strip()
        return price


    @allure.step('Получение стоимости поездки из активного тарифа')
    def giv_price_active_tarif(self):
        element = self.find_element_with_wait(MainLoc.PRICE_ACTIV_TARIF).text
        tarif = element.split()
        price = tarif[0]
        return price


    @allure.step('Наведение курсора на иконку информации')
    def navi_info_icon_tarif(self, info):
        self.click_to_element(info)
        self.hover_over_element(info)


    @allure.step('Цикл для поиска локаторов')
    def verify_elements_displayed(self, locators):
        for locator in locators:
            element = self.find_element_with_wait(locator)
            return  element

