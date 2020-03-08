from attributes.attribute_common import AttributeCommon as common


def test_open_page(wd, base_url):
    assert wd.current_url == base_url

