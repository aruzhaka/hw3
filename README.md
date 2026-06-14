# HW3 - Docker & Bash

## Структура проекта
- generator/ - Python-скрипт генерации CSV + Dockerfile
- reporter/ - Node.js-скрипт создания HTML-отчёта + Dockerfile
- data/ - сюда сохраняются сгенерированные файлы
- run.sh - главный скрипт управления

## Как запустить
./run.sh build_generator   # собрать образ генератора
./run.sh run_generator     # создать data/data.csv
./run.sh build_reporter    # собрать образ репортера
./run.sh run_reporter      # создать data/report.html
./run.sh structure         # показать структуру проекта
./run.sh clear_data        # очистить папку data/
./run.sh inside_generator  # посмотреть файлы внутри контейнера генератора
./run.sh inside_reporter   # посмотреть файлы внутри контейнера репортера
./run.sh report_server     # запустить веб-сервер с отчётом

## Просмотр отчёта через GitHub Codespaces

1. Склонировать репозиторий в GitHub Codespaces
2. Запуск всех команды по порядку:
   - ./run.sh build_generator
   - ./run.sh run_generator
   - ./run.sh build_reporter
   - ./run.sh run_reporter
   - ./run.sh report_server
3. В Codespaces открыть вкладку Ports (внизу в VS Code)
4. Найти порт 8080 и Open in Browser

Цепочка: браузер - Codespaces URL - порт 8080 на хосте Codespaces - порт 80 внутри nginx-контейнера - файл index.html примонтирован из папки data/
