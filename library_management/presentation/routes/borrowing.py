from uuid import UUID

from fastapi import APIRouter, HTTPException

from library_management.application.book_service import BookService
from library_management.infrastructure.repositories.Base_repository import \
    BookRepository

router = APIRouter()

# Initialize service
book_repo = BookRepository()
book_service = BookService(book_repo)


def raise_http_exception(status_code: int, detail: str):
    """Helper function to raise HTTPException."""
    raise HTTPException(status_code=status_code, detail=detail)


@router.post("/return/{book_id}")
def return_book(book_id: UUID):
    try:
        book_service.return_book(book_id)
    except ValueError as e:
        raise_http_exception(400, str(e))
    return {"detail": "Book returned successfully."}


@router.post("/{book_id}/{member_id}")
def borrow_book(book_id: UUID, member_id: UUID):
    try:
        book_service.borrow_book(book_id, member_id)
    except ValueError as e:
        raise_http_exception(400, str(e))
    return {"detail": "Book borrowed successfully."}
