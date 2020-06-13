from .locators_user_common import LocatorsUserCommon


class LocatorsMain(LocatorsUserCommon):
    SLIDESHOW = ("css", "#slideshow0")
    CAROUSE = ("css", "#carousel0")
    SLIDE_IPHONE = ("css", ".swiper-slide-active > a > img")
    SLIDE_MAC = ("css", ".swiper-slide-active img")
    SWITCH_ELEMENT = ("css", "#content")
    SWITCH = ("css", ".swiper-pagination-bullet-active")
    IN_CART = ("css", "[onclick=\"cart.add('%s');\"]")
    ALERT_SUCCESS = ("css", ".alert-success")
