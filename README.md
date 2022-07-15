# scrapy_parser_pep
___
## Обзор
Проект по парсингу документации pep. Для каждого pep-документа
собирает следующую информацию:
- номер 
- наименование 
- статус 

Сохраняет собранную информацию в csv-файлы.

## Требования
- Python 3.7

## Установка
- Клонировать репозиторий 
```commandline
git@github.com:AlxShvalev/scrapy_parser_pep.git
```
- Активировать виртуальное окружение
```commandline
python3 -m venv venv
```
- Установить зависимости
```commandline
pip install -r requirements.txt
```

## Запуск
Для запуска парсинга выполните команду
```commandline
scrapy crawl pep
```

---
### Автор
Алексей Швалёв