import requests

class Parser:
    def search_in_sites(self, word, sites):
        results = []
        for url in sites:
            try:
                response = requests.get(url, timeout=5)
                count = response.text.lower().count(word.lower())
                if count > 0:
                    results.append({"url": url, "count": count})
            except Exception as e:
                print(f"Помилка парсингу {url}: {e}")
        
        return sorted(results, key=lambda x: x['count'], reverse=True)