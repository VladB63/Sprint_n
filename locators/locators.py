from selenium.webdriver.common.by import By


class MainLocators:

    WAYPOINT_FIRST = By.XPATH, '//ymaps[text()="улица Хамовнический Вал, 34"]'
    WAYPOINT_SECOND = By.XPATH, '//ymaps[text()="Зубовский бульвар, 37"]'
    MARSHRUT_BLOCK = By.CLASS_NAME, 'type-picker'
    PRICE_AUTO = By.CLASS_NAME, 'text'
    STATUS_TIME_AUTO = By.CLASS_NAME, 'duration'
    OPTIMAL_BUTTON = By.XPATH, '//div[text()="Оптимальный"]'
    MINE_BUTTON = By.XPATH, '//div[text()="Свой"]'
    ACTIV_OPTIMAL_BUTTON = By.XPATH, '//div[@class="mode active" and text()="Оптимальный"]'
    ACTIV_MINE_BUTTON = By.XPATH, '//div[@class="mode active" and text()="Свой"]'
    ACTIV_TYPE_BUTTON = By.XPATH, '//div[@class="type active"]'
    CALL_TAXI_BUTTON = By.XPATH, '//button[text()="Вызвать такси"]'
    DRIVE_BUTTON = By.XPATH, '//div[@class="type drive"]'
    BOOKING_BUTTON = By.XPATH, '//button[text()="Забронировать"]'
    TARIF = By.XPATH, '//div[@class="tcard-title"]'
    ACTIV_TARIF = By.XPATH, '//div[@class="tcard active"]'

    TARIF_WORKING = By.XPATH, '//div[@class="tcard-title" and text()="Рабочий"]'
    TARIF_SLEEPY = By.XPATH, '//div[@class="tcard-title" and text()="Сонный"]'
    TARIF_VACATION = By.XPATH, '//div[@class="tcard-title" and text()="Отпускной"]'
    TARIF_TALKATIVE = By.XPATH, '//div[@class="tcard-title" and text()="Разговорчивый"]'
    TARIF_COMFORTING = By.XPATH, '//div[@class="tcard-title" and text()="Утешительный"]'
    TARIF_GLOSSY = By.XPATH, '//div[@class="tcard-title" and text()="Глянцевый"]'


    # INFO_TARIF_WORKING = By.XPATH, '//button[@data-for="tariff-card-0"]'
    INFO_TARIF_WORKING = By.XPATH, '//*[@id="tariff-card-0" and contains(@class, "tcard-i active")]'
    INFO_TARIF_SLEEPY = By.XPATH, '//button[@data-for="tariff-card-1"]'
    INFO_TARIF_VACATION = By.XPATH, '//button[@data-for="tariff-card-2"]'
    INFO_TARIF_TALKATIVE = By.XPATH, '//button[@data-for="tariff-card-3"]'
    INFO_TARIF_COMFORTING = By.XPATH, '//button[@data-for="tariff-card-4"]'
    INFO_TARIF_GLOSSY = By.XPATH, '//button[@data-for="tariff-card-5"]'


    # MODAL_INFO_WORKING = By.ID, 'tariff-card-0'
    MODAL_INFO_WORKING = By.XPATH, '//*[@id="tariff-card-0" and contains(@class, "show")]'
    # MODAL_INFO_SLEEPY = By.ID, 'tariff-card-1'
    MODAL_INFO_SLEEPY = By.XPATH, '//*[@id="tariff-card-1" and contains(@class, "show")]'
    MODAL_INFO_VACATION = By.ID, 'tariff-card-2'
    MODAL_INFO_TALKATIVE = By.ID, 'tariff-card-3'
    MODAL_INFO_COMFORTING = By.ID, 'tariff-card-4'
    MODAL_INFO_GLOSSY = By.ID, 'tariff-card-5'

    INPUT_FROM = By.ID, 'from'
    INPUT_WHERE = By.ID, 'to'

    FIELD_PHONE = By.XPATH, '//div[text()="Телефон"]'
    FIELD_PAYMENT = By.XPATH, '//label[text()="Комментарий водителю..."]'
    FIELD_COMMENT = By.XPATH, '//div[text()="Телефон"]'
    FIELD_REQUIREMENTS = By.XPATH, '//div[text()="Требования к заказу"]'
    LAPTOP_SLIDER = By.CLASS_NAME, 'switch'
    ORDER_BUTTON = By.XPATH, '//button[@class="smart-button"]'

    TITLE_SEARCH_CAR = By.XPATH, '//div[@class="order-header-title" and text()="Поиск машины"]'
    COUNTDOWN_TIMER = By.XPATH, '//div[@class="order-header-time"]'
    CANCEL_BUTTON = By.XPATH, '//button[@class="order-button"]/following-sibling::div[text()="Отменить"]'
    DETAIL_BUTTON = By.XPATH, '//button[@class="order-button"]/following-sibling::div[text()="Детали"]'

    WAIT_MIN = By.XPATH, '//div[@class="order-header-title" and text()=" мин. и приедет"]'
    CAR_NUMBER = By.XPATH, '//div[@class="number"]'
    CAR_IMAGE = By.XPATH, '//img[@src="/static/media/economy.61e4a774.svg" and alt="Car"]'
    VODILA_IMAGE = By.XPATH, '//img[@src="/static/media/bender.e90e5089.svg" and alt="Close"]'
    RATING_VODILA = By.CLASS_NAME, 'order-btn-rating'
    VODILA_NAME = By.XPATH, '//div[@class="order-button" and @style="cursor: default;"]'
    PRICE_TRIP = By.XPATH, '//button[@class="o-d-h" and text()="Еще про поездку"]/following-sibling::div[@class="o-d-sh"]'