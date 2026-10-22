# Check API
![Git](https://img.shields.io/badge/Git-2.54-F05032?style=flat-square&logo=git&logoColor=white) ![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)

Данный учебный скрипт позволяет получить HTTP-статус и тип передаваемых данных от GitHub API при помощи GET-запроса.
## Запуск с нуля
### 1. Клонирование репозитория
Клонируйте репозиторий с помощью команды:

```bash
git clone https://github.com/fant1es/python-learning.git
```
### 2. Переход к скрипту
В директории python-learning выполните:
```bash
cd .\week01\day01
```
Для следующих шагов **убедитесь**, что находитесь в данной директории.
### 3. Создание и активирование виртуального окружения
Для создания и активации виртуального окружения используйте следующие команды:
```bash
python -m venv .venv 

# Для Windows:
./.venv/Scripts/activate 

# Для Linux/macOS:
# source .venv/bin/activate 
```
### 4. Установление зависимостей
Зависимости указаны в requirements.txt. Для быстрой загрузки используйте команду:
```bash
pip install -r requirements.txt
```
### 5.  Использование 
Используйте команду:
```bash
# Для Windows (и большинства современных систем)
python -m check_api

# Для Linux / macOS (если python указывает на устаревшую версию)
python3 -m check_api
```

Примерный результат:
```
Обращаюсь к https://api.github.com...
Готово!
HTTP статус: 200
Значение content-type: application/json; charset=utf-8
```

Результат при ошибке:
```
Обращаюсь к https://api.github.com...
Ошибка подключения: не удалось установить соединение
```
Также программа вернет код возврата в зависимости от исключения