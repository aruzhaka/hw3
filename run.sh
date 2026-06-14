#!/bin/bash

COMMAND=$1
DATA_DIR="//c/Users/makoto/hw3/data"
export MSYS_NO_PATHCONV=1

case "$COMMAND" in

  build_generator)
    echo "Сборка образа генератора..."
    docker build -t generator ./generator
    ;;

  run_generator)
    echo "Запуск генератора — создаёт data/data.csv..."
    docker run --rm -v "$DATA_DIR":/data generator
    ;;

  create_local_data)
    echo "Создание data.csv локально в local_data/..."
    mkdir -p local_data
    python3 generator/generate.py local_data
    ;;

  build_reporter)
    echo "Сборка образа репортера..."
    docker build -t reporter ./reporter
    ;;

  run_reporter)
    echo "Запуск репортера — создаёт data/report.html..."
    docker run --rm -v "$DATA_DIR":/data reporter
    ;;

  structure)
    echo "Структура проекта:"
    find . -not -path './.git/*' | sort | sed 's|[^/]*/|  |g'
    ;;

  clear_data)
    echo "Удаление .csv и .html из data/..."
    rm -f data/*.csv data/*.html
    echo "Готово. Папка data/ теперь пустая."
    ;;

  inside_generator)
    echo "Содержимое /data внутри контейнера генератора:"
    docker run --rm -v "$DATA_DIR":/data generator ls -la /data
    ;;

  inside_reporter)
    echo "Содержимое /data внутри контейнера репортера:"
    docker run --rm -v "$DATA_DIR":/data reporter ls -la /data
    ;;

  report_server)
    echo "Запуск веб-сервера на порту 8080..."
    cp data/report.html data/index.html
    docker run --rm -p 8080:80 -v "$DATA_DIR":/usr/share/nginx/html:ro nginx:alpine
    ;;

  *)
    echo "Неизвестная команда: $COMMAND"
    ;;
esac