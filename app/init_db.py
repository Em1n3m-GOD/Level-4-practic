from app.db.db import Base, engine, SessionLocal
from app.db.crud import create_category, create_book

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
db = SessionLocal()

programming = create_category(db, "Программирование")
database = create_category(db, "Базы данных")

create_book(
    db,
    "Изучаем Python",
    "Книга по Python",
    1500,
    "",
    programming
)

create_book(
    db,
    "Fluent Python",
    "Продвинутый Python",
    3200,
    "",
    programming
)

create_book(
    db,
    "PostgreSQL",
    "Работа с PostgreSQL",
    2400,
    "",
    database
)

create_book(
    db,
    "SQLAlchemy",
    "ORM для Python",
    1800,
    "",
    database
)

db.close()

print("База данных заполнена.")