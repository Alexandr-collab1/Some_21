class Database:
    def __init__(self):
        self.sites = ["https://python.org", "https://google.com"]

    def add_site(self, url):
        if url not in self.sites:
            self.sites.append(url)
            print(f"БД: Сайт {url} додано.")

    def clear_all(self):
        self.sites = []
        print("БД: Очищено.")

    def get_all(self):
        return self.sites