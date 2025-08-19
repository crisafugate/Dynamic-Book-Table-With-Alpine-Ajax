from pydantic import BaseModel

class Book(BaseModel):
    isbn: str
    author: str
    title: str
    date: str
    pages: int
