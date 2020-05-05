class LocatorsUserCommon:
    # MENU
    YOUR_STORE = ("css", "Your Store")
    MENU_DESKTOPS = ("text", "Desktops")
    SELECT_ALL_DESKTOPS = ("text", "Show AllDesktops")

    # SEARCH
    INPUT_SEARCH = ("css", ".form-control.input-lg")
    SUBMIT_SEARCH = ("css", ".input-group-btn .btn-lg")

    # CATEGORIES
    GRID = ("css", "#grid-view")
    LIST = ("css", "#list-view")
    SORT = ("css", "#input-sort")
    SHOW_LIMIT = ("css", "#input-limit")
    COMPARE = ("css", "#compare-total")

    # COMMON BUTTONS
    IN_CART = ("css", "[onclick=\"cart.add('%s', '1');\"]")
    IN_WISHLIST = ("css", "[onclick=\"wishlist.add('%s');\"]")
    IN_COMPARE = ("css", "[onclick=\"compare.add('%s');\"]")

    # PRODUCTS
    MAC = ("css", '[alt="MacBook"]')
    IPHONE = ("css", '[alt="iPhone"]')
    APPLECINEMA = ("css", "[alt='Apple Cinema 30\"']")
    CANONEOS5D = ("css", '[alt="Canon EOS 5D"]')
    ID_MACBOOK = 43
    ID_APPLECINEMA = 42
    ID_CANONEOS5D = 30
    ID_HTC = 28
    ID_IPHONE = 40
    ID_ALMTREOPRO = 29
