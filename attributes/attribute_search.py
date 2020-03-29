from .attribute_common import AttributeCommon


class AttributeSearch(AttributeCommon):
    INPUT_SEARCH = ('css', '#input-search')
    SELECT_CATEGORIES = ('css', 'select[name="category_id"]')
    CHECKBOX_DESCRIPTION = ('css', '#description')
    CHECKBOX_SUBCATEGORIES = ('css', '[name="sub_category"]')
