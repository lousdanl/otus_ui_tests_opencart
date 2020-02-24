class Main:
    def __init__(self, wd, base_url):
        self.wd = wd
        self.base_url = base_url

    def open_page(self):
        self.wd.get(self.base_url)
