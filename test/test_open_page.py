from models.main import Main


def test_open_page(wd, base_url):
    main = Main(wd, base_url)
    main.open_page()
    assert wd.current_url == base_url

