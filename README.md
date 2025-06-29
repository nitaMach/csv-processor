# Руководство по установке и запуску CSV Processor

## 1. Установка системы

### Требования
- Python 3.8 или новее
- pip (обычно идет вместе с Python)
- Git (для скачивания из репозитория)

## 2. Скачивание проекта

```bash
# Клонирование репозитория
git clone https://github.com/yourusername/csv-processor.git
cd csv-processor
# Создание виртуального окружения (рекомендуется)
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# ИЛИ
venv\Scripts\activate     # Windows
```
## 3. Установка зависимостей

```bash
# Создание виртуального окружения (рекомендуется)
python -m venv venv
source venv/bin/activate  # Linux/MacOS
# ИЛИ
venv\Scripts\activate     # Windows
```

## 4. Запуск примеров
Пример CSV файла (products.csv)

| name             | brand   |   price |   rating |
|:-----------------|:--------|--------:|---------:|
| iphone 15 pro    | apple   |     999 |      4.9 |
| galaxy s23 ultra | samsung |    1199 |      4.8 |
| redmi note 12    | xiaomi  |     199 |      4.6 |
| iphone 14        | apple   |     799 |      4.7 |
| galaxy a54       | samsung |     349 |      4.2 |
| poco x5 pro      | xiaomi  |     299 |      4.4 |
| iphone se        | apple   |     429 |      4.1 |
| galaxy z flip 5  | samsung |     999 |      4.6 |
| redmi 10c        | xiaomi  |     149 |      4.1 |
| iphone 13 mini   | apple   |     599 |      4.5 |

Базовые команды:

```bash
# Установка основного пакета в режиме разработки
pip install -e .

# Установка дополнительных зависимостей для тестирования
pip install -e .[test]

# Просмотр справки
csv-processor --help

# Фильтрация данных
csv-processor --file example.csv --where "price>100"

# Сортировка данных
csv-processor --file  example.csv --order-by "price=desc"

# Агрегация данных
csv-processor --file  example.csv --aggregate "price=avg"

# Комбинированные операции (фильтрация + сортировка)
csv-processor --file  example.csv --where "price>50" --order-by "rating=desc"
```

## 5. Запуск тестов

```bash
# Запуск всех тестов
pytest -v
```




