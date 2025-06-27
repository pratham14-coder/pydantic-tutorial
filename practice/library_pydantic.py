from pydantic import BaseModel 
from typing import List, Optional 

class Book(BaseModel):
    Book_name: str
    Book_title: str
    Book_id: int
    Book_author: List[str] = None 
    Book_publisher_year: int 
    Book_subTitle: Optional[List[str]] = None 

book_object = {
    "Book_name": "JAVAx",
    "Book_title": "Introduction of java",
    "Book_id": 1001,
    "Book_publisher_year": 1991
}

def insert_book_data(book: Book):
    print("Book_name:", book.Book_name)
    print("Book_title:", book.Book_title)
    print("Book_id:", book.Book_id)
    print("Book_author:", book.Book_author)
    print("Book_publisher_year:", book.Book_publisher_year)
    print("Book_subTitle:", book.Book_subTitle)

book1 = Book(**book_object)

insert_book_data(book1)
