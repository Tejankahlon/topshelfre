# Python (FastAPI)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.testclient import TestClient

app = FastAPI()

class Book(BaseModel):
	id: int
	title: str
	author: str
	published_date: str
	price: float

books = []

@app.get("/books")
def get_books():
	return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
	book = next((bk for bk in books if bk.id == book_id), None)
	if book is None:
		raise HTTPException(status_code=404, detail="Book not found")
	return book 

@app.post("/books") 
def create_book(book: Book):
	if any(bk.id == book.id for bk in books):
		raise HTTPException(status_code=400, detail="Book already exists")
	books.append(book)
	return book

@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
	index = next((i for i, bk in enumerate(books) if bk.id == book_id), None)
	if index is None:
		raise HTTPException(status_code=404, detail="Book not found")
	books[index] = book
	return book

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
	index = next((i for i, bk in enumerate(books) if bk.id == book_id), None)
	if index is None:
		raise HTTPException(status_code=404, detail="Book not found")
	books.pop(index)
	return {"message": "Book deleted"}

@app.search("/search")
def search_books(q: str):
	results = [book for book in books if q.lower() in book.title.lower() or q.lower() in book.author.lower()]
	return results if results else {"message": "No books found matching the search"}

#Tests

client = TestClient(app)

def test_create_book():
	response = client.post("/books", json={"id": 1, "title": "Book 1", "author": "Author 1", "published_date": "2022-01-01", "price": 9.99})
	assert response.status_code == 201
	assert response.json() == {"id": 1, "title": "Book 1", "author": "Author 1", "published_date": "2022-01-01", "price": 9.99}

def test_get_book():
	response = client.get("/books/1")
	assert response.status_code == 200
	assert response.json() == {"id": 1, "title": "Book 1", "author": "Author 1", "published_date": "2022-01-01", "price": 9.99}

def test_update_book():
	response = client.put("/books/1", json={"title": "Updated Book 1", "author": "Updated Author 1", "published_date": "2022-01-02", "price": 19.99})
	assert response.status_code == 200
	assert response.json() == {"id": 1, "title": "Updated Book 1", "author": "Updated Author 1", "published_date": "2022-01-02", "price": 19.99}

def test_delete_book():
	response = client.delete("/books/1")
	assert response.status_code == 200
	assert response.json() == {"message": "Book deleted"}

def test_get_books():
	response = client.get("/books")
	assert response.status_code == 200
	assert response.json() == []

def test_search_books():
	client.post("/books", json={id:2, "title": "Different Book", "author": "Different Author", "published_date": "2022-01-01", "price": 15.99})
	response = client.get("/search?query=Different")
	assert response.status_code == 200
	assert len(response.json()) > 0

	response = client.get("/search?query=Something_random")
	assert response.status_code == 200 
	assert response.json() == {"message": "No books found matching the search"}





