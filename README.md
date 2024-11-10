# qutes_parser
Проект для извлечения цитат с сайта [Quotes to Scrape](https://quotes.toscrape.com/)

## Что было сделано в рамках проекта?

- **Парсинг веб-страниц:** Код осуществляет парсинг веб-страниц с сайта [Quotes to Scrape](https://quotes.toscrape.com/).
- **Извлечение цитат:** Из каждой страницы извлекаются цитаты, авторы и соответствующие теги.
- **Формирование структуры данных:** Извлеченные данные преобразуются в структуру данных в виде словаря Python.
- **Сохранение данных:** Полученные данные сохраняются в формате JSON для последующего использования.



### Структура проекта:
```
ilshat2
 └── qutes_parser
     ├── .gitignore
     ├── README.md
     ├── parser.py    <-- файл с кодом
     ├── quotes.json  <-- файл с цитатами
