from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db import crud
from app import schemas

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[schemas.BookResponse])
def get_books(db: Session = Depends(get_db)):
    return crud.get_books(db)


@router.get("/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")

    return book


@router.post("/", response_model=schemas.BookResponse, status_code=201)
def create_book(book: schemas.BookCreate,
                db: Session = Depends(get_db)):

    category = crud.get_category(db, book.category_id)

    if not category:
        raise HTTPException(status_code=404, detail="Категория не найдена")

    return crud.create_book(
        db,
        book.title,
        book.description,
        book.price,
        book.url,
        category
    )


@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int,
                data: schemas.BookCreate,
                db: Session = Depends(get_db)):

    category = crud.get_category(db, data.category_id)

    if not category:
        raise HTTPException(status_code=404, detail="Категория не найдена")

    book = crud.update_book(
        db,
        book_id,
        data.title,
        data.description,
        data.price,
        data.url,
        category
    )

    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")

    return book


@router.delete("/{book_id}")
def delete_book(book_id: int,
                db: Session = Depends(get_db)):

    book = crud.delete_book(db, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")

    return {"message": "Книга удалена"}