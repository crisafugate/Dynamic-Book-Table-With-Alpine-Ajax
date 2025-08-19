import uvicorn
from fastapi import FastAPI, Request
from routes.books import books_router

app = FastAPI()
app.include_router(books_router)


if __name__ == '__main__':
    uvicorn.run('index:app', reload=True)
