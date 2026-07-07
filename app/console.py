from app.db.db import SessionLocal
from app.db.crud import get_categories, get_books

db = SessionLocal()

print("=== Категории ===")
for category in get_categories(db):
    print(f"{category.id}. {category.title}")

print("\n=== Книги ===")
for book in get_books(db):
    print(f"{book.id}. {book.title}")
    print(f"   Описание: {book.description}")
    print(f"   Цена: {book.price}")
    print(f"   Категория: {book.category.title}")
    print()

db.close()