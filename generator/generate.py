import csv
import random
import os
import sys

NUM_ROWS = 50

COLUMNS = ["title", "author", "price", "genre", "in_stock"]

def generate_row():
    books = [
        ("Confessions of a Mask", "Yukio Mishima"),
        ("The Sound of Waves", "Yukio Mishima"),
        ("The Temple of the Golden Pavilion", "Yukio Mishima"),
        ("The Bell Jar", "Sylvia Plath"),
        ("Ariel", "Sylvia Plath"),
        ("Mrs Dalloway", "Virginia Woolf"),
        ("To the Lighthouse", "Virginia Woolf"),
        ("The Waves", "Virginia Woolf"),
        ("Pride and Prejudice", "Jane Austen"),
        ("Sense and Sensibility", "Jane Austen"),
        ("Emma", "Jane Austen"),
        ("Bonjour Tristesse", "Françoise Sagan"),
        ("A Certain Smile", "Françoise Sagan"),
        ("The Kindly Ones", "Jonathan Littell"),
        ("A Game of Thrones", "George R.R. Martin"),
        ("A Storm of Swords", "George R.R. Martin"),
        ("1984", "George Orwell"),
        ("Brave New World", "Aldous Huxley"),
        ("We", "Yevgeny Zamyatin"),
        ("The Suitcase", "Sergei Dovlatov"),
        ("The Zone", "Sergei Dovlatov"),
        ("The Compromise", "Sergei Dovlatov"),
    ]

    title, author = random.choice(books)

    genre_map = {
        "Yukio Mishima": "Literary Fiction",
        "Sylvia Plath": "Poetry & Fiction",
        "Virginia Woolf": "Modernism",
        "Jane Austen": "Classic",
        "Françoise Sagan": "French Literature",
        "Jonathan Littell": "Historical Fiction",
        "George R.R. Martin": "Fantasy",
        "George Orwell": "Dystopia",
        "Aldous Huxley": "Dystopia",
        "Yevgeny Zamyatin": "Dystopia",
        "Sergei Dovlatov": "Russian Literature",
    }

    return {
        "title": title,
        "author": author,
        "price": round(random.uniform(5.0, 35.0), 2),
        "genre": genre_map[author],
        "in_stock": random.randint(0, 50),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)