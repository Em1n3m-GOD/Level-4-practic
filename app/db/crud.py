from app.db.models import Category, Book


# ---------- CATEGORY ----------

def create_category(db, title):
    category = Category(title=title)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def get_categories(db):
    return db.query(Category).all()


def get_category(db, category_id):
    return db.query(Category).filter(Category.id == category_id).first()


def update_category(db, category_id, title):
    category = get_category(db, category_id)
    if not category:
        return None

    category.title = title
    db.commit()
    db.refresh(category)
    return category


def delete_category(db, category_id):
    category = get_category(db, category_id)
    if not category:
        return None

    db.delete(category)
    db.commit()
    return category


# ---------- BOOK ----------

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


def get_books(db):
    return db.query(Book).all()


def get_book(db, book_id):
    return db.query(Book).filter(Book.id == book_id).first()


def update_book(db, book_id, title, description, price, url, category):
    book = get_book(db, book_id)
    if not book:
        return None

    book.title = title
    book.description = description
    book.price = price
    book.url = url
    book.category = category

    db.commit()
    db.refresh(book)
    return book


def delete_book(db, book_id):
    book = get_book(db, book_id)
    if not book:
        return None

    db.delete(book)
    db.commit()
    return book