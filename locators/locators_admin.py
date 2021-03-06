class LocatorsAdmin:
    URL_ADMIN = "admin"

    # LOGIN
    LOGIN_FORM = ("css", ".panel-default")
    USERNAME = ("css", "#input-username")
    PASSWORD = ("css", "#input-password")
    LOGIN = ("css", ".btn-primary")
    FORGOTTEN_PASSWORD = ("text", "Forgotten Password")
    LOGOUT = ("css", ".nav li span")

    # MENU
    CATALOG = "#collapse1"
    PRODUCTS = ("css", "#collapse1 > li:nth-child(2) > a")
    ATTRIBUTE_HREF = "href"

    # BUTTONS
    ADD_PRODUCT = ("css", '[data-original-title="Add New"]')
    BUTTON_SAVE = ("css", '[data-original-title="Save"]')
    BUTTON_DELETE = ("css", '[data-original-title="Delete"]')
    BUTTON_EDIT = ("css", '[data-original-title="Edit"]')
    BUTTON_COPY = ("css", '[data-original-title="Copy"]')
    BUTTON_CLOSE = ("css", "#filemanager .modal-header .close")
    BUTTON_CANCEL_EDIT = ("css", '[data-original-title="Cancel"]')

    # EDIT PRODUCT
    TAB_GENERAL = ("css", '[href="#tab-general"]')
    TAB_DATA = ("css", '[href="#tab-data"]')
    TAB_SPECIAL = ("css", '[href="#tab-special"]')
    TAB_IMAGE = ("css", '[href="#tab-image"]')
    PRODUCT_NAME = ("css", "#input-name1")
    META_TAG_TITLE = ("css", "#input-meta-title1")
    MODEL = ("css", "#input-model")
    PRICE_TAB_DATA = ("css", "#input-price")
    PRICE_TAB_SECTION = ("css", "#special-row0 > td:nth-child(3) > input")
    QUANTITY = ("css", "#input-quantity")
    STATUS = ("css", "#input-status")
    SORT = ("css", "#input-sort-order")

    # ELEMENTS
    COUNT_PAGES = ("css", ".col-sm-6.text-right")
    PRODUCTS_ON_PAGE = ("css", "tbody tr")
    TABLE_PROD_NAME = ("css", ".text-left")
    TABLE_PROD_PRICE = ("css", ".text-right")
    PRICE_BEFORE = ("css", '[style="text-decoration: line-through;"]')
    PRICE_AFTER = ("css", ".text-danger")
    ELEMENT_PAGINATION = ("css", ".pagination")
    NEXT_PAGE = ("xpath", "//*[text()='>']")
    FIRST_PAGE = ("xpath", "//*[text()='1']")
    LAST_PAGE = ("xpath", "//*[text()='>|']")
    PREVIOUS_PAGE = ("xpath", "//*[text()='<']")
    PRODUCT_CHECKBOX = ("css", '[type="checkbox"]')

    # ALERTS
    ALERT_WARNING = ("css", ".alert-danger.alert-dismissible")
    TEXT_WARNING_ALERT = "Warning: Please check the form carefully for errors!"
    DANGER_TEXT = ("css", ".text-danger")
    ALERT_SUCCESS = ("css", ".alert-success")

    # INPUT IMAGE
    EDIT_IMAGE = ("css", ".img-thumbnail img")
    BUTTON_EDIT_IMAGE = ("css", "#button-image i")
    BUTTON_UPLOAD = ("css", "#button-upload")
    ATTRIBUTE_IMAGE = ("css", '[alt="%s"]')
    CHECKBOX_IMAGE = ("css", '[value="catalog/%s"]')
    FORM_INPUT = ("css", "#form-upload")
    INPUT_FILE = ("css", "input[type='file']")

    # SCRIPTS
    SCRIPT_FIND_ATTRIBUTES = (
        "var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { "
        "items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; "
        "return items; "
    )

    SELECT_PRODUCT_BY_ID = ("xpath", '//input[@value="%s"]/../..')
