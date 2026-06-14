# HW3 — Docker & Bash

## Структура проекта
- `generator/` — Python-скрипт генерации CSV + Dockerfile
- `reporter/` — Node.js-скрипт создания HTML-отчёта + Dockerfile
- `data/` — сюда сохраняются сгенерированные файлы
- `run.sh` — главный скрипт управления

## Как запустить

```bash
./run.sh build_generator   # собрать образ генератора
./run.sh run_generator     # создать data/data.csv
./run.sh build_reporter    # собрать образ репортера
./run.sh run_reporter      # создать data/report.html
```

## Просмотр отчёта через GitHub Codespaces

1. Запустите веб-сервер: `./run.sh report_server`
2. В Codespaces откройте вкладку **Ports** (внизу в VS Code)
3. Найдите порт **8080** и нажмите **Open in Browser**
4. Codespaces автоматически создаёт публичный URL — по нему откроется `report.html`

Цепочка: браузер - Codespaces URL - порт 8080 на хосте Codespaces - порт 80 внутри nginx-контейнера - файл report.html примонтирован из папки data/