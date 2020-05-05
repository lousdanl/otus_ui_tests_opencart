from .locators_user_common import LocatorsUserCommon


class LocatorsProduct(LocatorsUserCommon):
    CONTENT = ("css", "#content")
    NAME_PRODUCT = ("css", "h1")
    PRICE = ("css", "h2")
    OPTION226 = ("css", "#input-option226")
    QUANTITY = ("css", "#input-quantity")
    IN_CART = ("css", "#button-cart")
    TAG_DESCRIPTION = ("css", '[href="#tab-description"]')
    DESCRIPTION = ("css", "#tab-description")
    TAG_REVIEWS = ("css", '[href="#tab-review"]')
    INPUT_NAME = ("css", "#input-name")
    INPUN_REVIEW = ("css", "#input-review")
    RAITING = ("css", 'input[name="rating"][value="%s"]')
    CONTINUE = ("css", "#button-review")
    IMAGE_ADDITIONAL = ("css", ".image-additional a")
    IMAGE_OPEN = ("css", ".mfp-figure")
    IMAGE_CLOSE = ("css", ".mfp-close")
    NEXT_IMAGE = ("css", '[title="Next (Right arrow key)"]')
    ALERT_SUCCESS = ("css", ".alert-success")
    ALERT_TEXT_TO_CART = "Success: You have added %s to your shopping cart!"
