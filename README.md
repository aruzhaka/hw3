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
