from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from models.books import Book
from config.database import conn
from schemas.books import bookRecord, listOfBookRecords
from bson import ObjectId
from fastapi.templating import Jinja2Templates

books_router = APIRouter()
templates = Jinja2Templates(directory='templates')

def convert_to_html(books):
    html = '<thead><tr>'
    html += '<th x-show="isbn">ISBN</th>'
    html += '<th x-show="author">Author</th>'
    html += '<th x-show="title">Title</th>'
    html += '<th x-show="date">Date</th>'
    html += '<th x-show="pages">Pages</th>'
    html += '</tr></thead><tbody>'

    for b in books:
        html += f'<tr><td x-show="isbn">{b["isbn"]}</td><td x-show="author">{b["author"]}</td>'
        html += f'<td x-show="title">{b["title"]}</td><td x-show="date">{b["date"]}</td>'
        html += f'<td x-show="pages">{str(b["pages"])}</td></tr>'

    html += '</tbody>'
    return html

@books_router.get('/books', response_class=HTMLResponse)
async def find_all_books(request: Request):
    books = listOfBookRecords(conn.local.books.find())
    book_html = convert_to_html(books) 
    context = {'request': request, 'books': book_html}
    return templates.TemplateResponse("books.html", context)

@books_router.post('/books', response_class=HTMLResponse)
async def find_books_by_author(author: str = Form()):
    books = listOfBookRecords(conn.local.books.find({ 'author': author }))
    book_html = f'<table id="books">{convert_to_html(books)}</table>'
    return book_html

@books_router.post('/books')
async def create_bookrecord(book: Book):
    conn.local.books.insert_one(dict(book))
    return listOfBookRecords(conn.local.books.find())

@books_router.get('/books/{bookId}')
async def get_salesrecord(bookId):
    return bookRecord(conn.local.books.find_one({"_id": ObjectId(bookId)}))

@books_router.delete('/books/{bookId}')
async def delete_bookrecord(bookId):
    return bookRecord(conn.local.books.find_one_and_delete({"_id": ObjectId(bookId)}))
