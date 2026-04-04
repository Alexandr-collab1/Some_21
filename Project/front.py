import tkinter as tk

class AppInterface:
    def __init__(self, db_obj, parser_obj):
        self.db = db_obj
        self.parser = parser_obj
        
        self.window = tk.Tk()
        self.window.title("Пошукова система")
        self.window.geometry("500x600")


        tk.Label(self.window, text="Введіть посилання або слово для пошуку:").pack(pady=5)
        self.entry = tk.Entry(self.window, width=50)
        self.entry.pack(pady=10)


        self.btn_add = tk.Button(self.window, text="Додати сайт в БД", command=self.add_to_db)
        self.btn_add.pack(pady=5)

        self.btn_search = tk.Button(self.window, text="Шукати слово на сайтах", command=self.run_search)
        self.btn_search.pack(pady=5)


        self.btn_clear = tk.Button(self.window, text="Очистити базу", command=self.clear_db)
        self.btn_clear.pack(pady=5)


        self.result_l = tk.Label(self.window, text="База порожня", justify="left", wraplength=450)
        self.result_l.pack(pady=20)

    def add_to_db(self):
        url = self.entry.get()
        if url.startswith("http"): 
            self.db.add_site(url)
            self.entry.delete(0, tk.END) 
            self.result_l.config(text=f"Сайт {url} успішно додано!")
        else:
            self.result_l.config(text="Помилка: посилання має починатися з http або https")

    def run_search(self):
        word = self.entry.get()
        sites = self.db.get_all()
        
        if not sites:
            self.result_l.config(text="Спочатку додайте хоча б один сайт!")
            return

        self.result_l.config(text="Йде пошук... зачекайте...")
        self.window.update() 

        results = self.parser.search_in_sites(word, sites)
        
        if not results:
            self.result_l.config(text=f"Слово '{word}' не знайдено на жодному сайті.")
        else:
            display_text = "Результати (за рейтингом):\n"
            for r in results:
                display_text += f"[{r['count']} згадок] - {r['url']}\n"
            self.result_l.config(text=display_text)

    def clear_db(self):
        self.db.clear_all()
        self.result_l.config(text="Базу сайтів повністю очищено.")

    def run(self):
        self.window.mainloop()