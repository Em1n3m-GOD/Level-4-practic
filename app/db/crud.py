from app.db.models import Category, Book


def create_category(db, title):
    category = Category(title=title)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def create_book(db, title, description, price, url, category):
    book = Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category=category
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def get_categories(db):
    return db.query(Category).all()


def get_books(db):
    return db.query(Book).all()