import requests
from bs4 import BeautifulSoup

# Адреса сайту
url = "http://books.toscrape.com"

# Отримуємо вміст сторінки
response = requests.get(url)
response.encoding = 'utf-8'

# Створюємо об'єкт BeautifulSoup для аналізу HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Знаходимо всі контейнери з книгами
books = soup.find_all('article', class_='product_pod')

print(f"{'Назва книги':<50} | {'Ціна'}")
print("-" * 65)

# Проходимо циклом по кожній знахідці
for book in books:
    # Завдання 1: Витягуємо назву (вона в атрибуті title тегу a)
    # Ми беремо саме атрибут title, бо текст у посиланні може бути скороченим (з трьома крапками)
    title = book.h3.a['title']
    
    # Завдання 2: Витягуємо ціну
    price = book.find('p', class_='price_color').text
    
    # Завдання 3: Виведення повної інформації
    print(f"{title[:47] + '...' if len(title) > 47 else title:<50} | {price}")