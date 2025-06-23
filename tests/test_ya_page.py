import allure
import pytest
from pages.main_page import MainPage
from locators.locators import MainLocators
from data import DataPage

class TestYAPage:

    # @allure.title('Проверка отображения точек назначения на карте')
    # def test_point_from_where(self, driver):
    #     ya_praktik = MainPage(driver)
    #     ya_praktik.open_url()
    #     ya_praktik.point_from_where()
    #     first_point = ya_praktik.find_first_poit_in_card()
    #     second_poit = ya_praktik.find_second_poit_in_card()
    #     assert first_point.is_displayed() and second_poit.is_displayed()
    #
    #
    # @allure.title('Проверка отображения блока маршрута')
    # def test_marshrut_block(self, driver):
    #     ya_praktik = MainPage(driver)
    #     ya_praktik.open_url()
    #     ya_praktik.point_from_where()
    #     marshrut_block = ya_praktik.find_marshrut_block()
    #     assert marshrut_block.is_displayed()
    #
    #
    # @allure.title('Проверка реакции на ввод одного и того же адреса')
    # @pytest.mark.parametrize(
    #     "address", [
    #         DataPage.POINT_ADDRESS_FROM
    #     ]
    # )
    # def test_double_address_from_where(self, driver, address):
    #     ya_praktik = MainPage(driver)
    #     ya_praktik.open_url()
    #     ya_praktik.dubl_point_from(address)
    #     price = ya_praktik.giv_price_auto()
    #     status = ya_praktik.giv_status_and_time_auto()
    #     assert price == 'Авто Бесплатно' and status == 'В пути 0 мин.'
    #
    #
    # @allure.title('Проверка смены вида маршрута с пересчетом данных')
    # def test_change_type_route_recalculating_data(self, driver):
    #     ya_praktik = MainPage(driver)
    #     ya_praktik.open_url()
    #     ya_praktik.point_from_where()
    #     ya_praktik.click_optimal_button()
    #     activ_tab = ya_praktik.find_active_tab_optimal()
    #     price = ya_praktik.giv_price_auto()
    #     status = ya_praktik.giv_status_and_time_auto()
    #     assert activ_tab.is_displayed() and price == 'Авто ~ 40 руб.' and status == 'В пути 3 мин.'
    #
    #
    # @allure.title('Проверка смены вида маршрута с доп типами передвижений')
    # def test_type_route_add_type(self, driver):
    #     ya_praktik = MainPage(driver)
    #     ya_praktik.open_url()
    #     ya_praktik.point_from_where()
    #     ya_praktik.click_mine_button()
    #     activ_tab = ya_praktik.find_active_tab_mine()
    #     activ_type = ya_praktik.find_active_tab_type()
    #     assert activ_tab.is_displayed() and activ_type.is_displayed()
    #
    #
    #
    # @allure.title('Проверка наличия кнопки Вызвать такси')
    # def test_type_route_add_type(self, driver):
    #     ya_praktik = MainPage(driver)
    #     ya_praktik.open_url()
    #     ya_praktik.point_from_where()
    #     call_button = ya_praktik.find_call_button()
    #     assert call_button.is_displayed()
    #
    #
    # @allure.title('Проверка наличия кнопки Забронировать')
    # def test_booking_button(self, driver):
    #     ya_praktik = MainPage(driver)
    #     ya_praktik.open_url()
    #     ya_praktik.point_from_where()
    #     ya_praktik.click_mine_button()
    #     ya_praktik.click_drive_button()
    #     booking = ya_praktik.find_booking_button()
    #     assert booking.is_displayed()
    #
    #
    # @allure.title('Проверка списка тарифов')
    # def test_tarif_list(self, driver):
    #     ya_praktik = MainPage(driver)
    #     ya_praktik.open_url()
    #     ya_praktik.point_from_where()
    #     ya_praktik.click_call_taxi_button()
    #     tarifs = ya_praktik.get_tarif_list()
    #     activ_tarif = ya_praktik.find_active_tarif()
    #     assert tarifs == DataPage.All_TARIF and activ_tarif.is_displayed()

    # Этот падает
    @allure.title('Проверка описания тарифа')
    @pytest.mark.parametrize(
        "tarif,info,modal", [
            (MainLocators.TARIF_WORKING, MainLocators.INFO_TARIF_WORKING, MainLocators.MODAL_INFO_WORKING),
            (MainLocators.TARIF_SLEEPY, MainLocators.INFO_TARIF_SLEEPY, MainLocators.MODAL_INFO_SLEEPY)
            # (MainLocators.TARIF_VACATION, MainLocators.INFO_TARIF_VACATION, MainLocators.MODAL_INFO_VACATION),
            # (MainLocators.TARIF_TALKATIVE, MainLocators.INFO_TARIF_TALKATIVE, MainLocators.MODAL_INFO_TALKATIVE),
            # (MainLocators.TARIF_COMFORTING, MainLocators.INFO_TARIF_COMFORTING, MainLocators.MODAL_INFO_COMFORTING),
            # (MainLocators.TARIF_GLOSSY, MainLocators.INFO_TARIF_GLOSSY, MainLocators.MODAL_INFO_GLOSSY)
        ]
    )
    def test_tarif_description(self, driver, tarif, info, modal):
        ya_praktik = MainPage(driver)
        ya_praktik.open_url()
        ya_praktik.point_from_where()
        ya_praktik.click_call_taxi_button()
        ya_praktik.click_tarif_button(tarif)
        ya_praktik.navi_info_icon_tarif(info)
        info_window = ya_praktik.find_modal_info_window(modal)
        assert info_window.is_displayed()


    # @allure.title('Проверка Блока с полями Телефон, Способ оплаты, Комментарий водителю,'
    #               ' Требования к заказу')
    # def test_fields_block_selection(self, driver):
    #     ya_praktik = MainPage(driver)
    #     ya_praktik.open_url()
    #     ya_praktik.point_from_where()
    #     ya_praktik.click_call_taxi_button()
    #     fields = [
    #         MainLocators.FIELD_PHONE,
    #         MainLocators.FIELD_PAYMENT,
    #         MainLocators.FIELD_COMMENT,
    #         MainLocators.FIELD_REQUIREMENTS
    #     ]
    #     element = ya_praktik.verify_elements_displayed(fields)
    #     assert element.is_displayed()


    # @allure.title('Проверка окна ожидания')
    # def test_details_waiting_window(self, driver):
    #     ya_praktik = MainPage(driver)
    #     ya_praktik.open_url()
    #     ya_praktik.point_from_where()
    #     ya_praktik.click_call_taxi_button()
    #     ya_praktik.click_details_button()
    #     ya_praktik.click_laptop_table_button()
    #     ya_praktik.click_order_button()
    #     details_in_modal = [
    #         MainLocators.TITLE_SEARCH_CAR,
    #         MainLocators.COUNTDOWN_TIMER,
    #         MainLocators.CANCEL_BUTTON,
    #         MainLocators.DETAIL_BUTTON
    #     ]
    #     element = ya_praktik.verify_elements_displayed(details_in_modal)
    #     assert element.is_displayed()


    # @allure.title('Проверка окна оформленного заказа')
    # def test_details_completed_order(self, driver):
    #     ya_praktik = MainPage(driver)
    #     ya_praktik.open_url()
    #     ya_praktik.point_from_where()
    #     ya_praktik.click_call_taxi_button()
    #     ya_praktik.click_details_button()
    #     ya_praktik.click_laptop_table_button()
    #     ya_praktik.click_order_button()
    #     details_in_modal = [
    #         MainLocators.WAIT_MIN,
    #         MainLocators.CAR_NUMBER,
    #         MainLocators.CAR_IMAGE,
    #         MainLocators.VODILA_NAME,
    #         MainLocators.VODILA_IMAGE,
    #         MainLocators.RATING_VODILA,
    #         MainLocators.CANCEL_BUTTON,
    #         MainLocators.DETAIL_BUTTON
    #     ]
    #     element = ya_praktik.verify_elements_displayed(details_in_modal)
    #     assert element.is_displayed()





