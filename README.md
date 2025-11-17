# Project: Working with Weakly Structured Data Types

## Description
This Python project demonstrates working with weakly structured data types by generating synthetic user data and converting it between different formats. The project consists of two main components:

1. **Data Generation** (`main.py`): Creates synthetic user data with nested structures and saves it as JSON
2. **Data Conversion** (`dsv_convert.py`): Converts the JSON data into delimited-separated value (DSV) format with proper normalization

## Features
- Generates realistic synthetic user data with complex nested structures
- Handles various data types including strings, lists, dictionaries, and dates
- Converts nested JSON data into flat DSV tables (users, publications, reviews)
- Supports custom delimiters for DSV output
- Calculates additional metrics like word count in reviews

## Project Structure
```
├── main.py                 # Data generation module
├── dsv_convert.py          # Data conversion module
├── users_data.json         # Generated JSON data (output)
├── users_table.dsv         # Users table in DSV format (output)
├── publications_table.dsv  # Publications table in DSV format (output)
└── reviews_table.dsv       # Reviews table in DSV format (output)
```

## Installation & Usage
1. Clone the repository
2. Run the data generator:
   ```bash
   python main.py
   ```
3. Convert the generated data:
   ```bash
   python dsv_convert.py
   ```

## Data Model
The project handles the following entities:
- **Users**: Personal information, registration data, status
- **Publications**: User-created content with metadata
- **Reviews**: User reviews for publications with text analysis

## Requirements
- Python 3.6+
- Standard libraries only (no external dependencies)

---

# Проект: Работа со слабоструктурированными типами данных

## Описание
Этот проект на Python демонстрирует работу со слабоструктурированными типами данных путем генерации синтетических пользовательских данных и их преобразования между различными форматами. Проект состоит из двух основных компонентов:

1. **Генерация данных** (`main.py`): Создает синтетические пользовательские данные с вложенной структурой и сохраняет в формате JSON
2. **Преобразование данных** (`dsv_convert.py`): Конвертирует JSON-данные в формат значений с разделителями (DSV) с правильной нормализацией

## Возможности
- Генерация реалистичных синтетических пользовательских данных со сложной вложенной структурой
- Работа с различными типами данных: строки, списки, словари, даты
- Преобразование вложенных JSON-данных в плоские DSV-таблицы (пользователи, публикации, отзывы)
- Поддержка пользовательских разделителей для DSV-вывода
- Расчет дополнительных метрик (количество слов в отзывах)

## Структура проекта
```
├── main.py                 # Модуль генерации данных
├── dsv_convert.py          # Модуль преобразования данных
├── users_data.json         # Сгенерированные JSON-данные (результат)
├── users_table.dsv         # Таблица пользователей в DSV-формате (результат)
├── publications_table.dsv  # Таблица публикаций в DSV-формате (результат)
└── reviews_table.dsv       # Таблица отзывов в DSV-формате (результат)
```

## Установка и использование
1. Клонируйте репозиторий
2. Запустите генератор данных:
   ```bash
   python main.py
   ```
3. Преобразуйте сгенерированные данные:
   ```bash
   python dsv_convert.py
   ```

## Модель данных
Проект работает со следующими сущностями:
- **Пользователи**: Персональная информация, данные регистрации, статус
- **Публикации**: Созданный пользователями контент с метаданными
- **Отзывы**: Пользовательские отзывы на публикации с анализом текста

## Требования
- Python 3.6+
- Только стандартные библиотеки (внешние зависимости не требуются)
