# qutes_parser
Проект для извлечения цитат с сайта [Quotes to Scrape](https://quotes.toscrape.com/)

## Что было сделано в рамках проекта?

- **Парсинг веб-страниц:** Код осуществляет парсинг веб-страниц с сайта [Quotes to Scrape](https://quotes.toscrape.com/).
- **Извлечение цитат:** Из каждой страницы извлекаются цитаты, авторы и соответствующие теги.
- **Формирование структуры данных:** Извлеченные данные преобразуются в структуру данных в виде словаря Python.
- **Сохранение данных:** Полученные данные сохраняются в формате 'JSON' для последующего использования.

## Как осуществлялся сбор данных?

- **Отправка HTTP-запросов:** Для получения HTML-кода страниц использовалась библиотека requests.
- **Парсинг HTML:** Библиотека `BeautifulSoup` использовалась для анализа HTML-кода и извлечения необходимой информации.
- **Извлечение данных:** С помощью методов 'find_all' и 'find' находились нужные элементы HTML-структуры, содержащие цитаты, авторов и теги.
- **Формирование структуры данных:** Извлеченные данные преобразовывались в словари Python для удобства дальнейшей обработки.
- **Сохранение данных:** Полученные словари сохранялись в формате 'JSON' в файл 'quotes.json.'

## Почему были выбраны определенные методы и инструменты?

- **requests:** Эта библиотека является стандартным инструментом для отправки HTTP-запросов в Python. Она проста в использовании и обеспечивает надежную работу.
- **BeautifulSoup:** Является мощным инструментом для парсинга 'HTML' и 'XML'. Она предоставляет удобный интерфейс для поиска элементов по различным критериям.
- **JSON:** Формат JSON широко используется для обмена данными и легко читается как людьми, так и машинами. Он идеально подходит для сохранения структурированных данных, таких как полученные цитаты.
Выбор этих инструментов обусловлен их простотой использования, эффективностью и широкой поддержкой в сообществе Python.

### Структура проекта:
```
ilshat2
 └── qutes_parser
     ├── .gitignore
     ├── README.md
     ├── parser.py    <-- файл с кодом
     ├── quotes.json  <-- файл с цитатами
