from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import odoorpc

app = FastAPI()

# Configuration de la connexion Odoo
odoo = odoorpc.ODOO('localhost', port=8069)
odoo.login('library_manager', 'karnold@svsburkina.com', 'hoodoo')

if 'book_model' not in odoo.env:
    raise HTTPException(status_code=500, detail="The model 'book_model' does not exist in the database")


# Modèle Pydantic pour les livres
class Book(BaseModel):
    name: str
    author: str
    published_date: str = None
    isbn: str = None


#The error message dictionary
errors_dict = {
    10: {"eng": "Book not found", "fr": "Livre non trouvé"}
}
#The success message dictionary
success_dict = {
    1: {"eng": "Book created successfully", "fr": "Livre crée avec succès"},
    2: {"eng": "Book updated successfully", "fr": "Livre mis à jour avec succès"},
    3: {"eng": "Book deleted successfully", "fr": "Livre supprimé avec succès"}
}


#This endpoint create a book with the data sent in the request body
@app.post("/api/books")
def add_book(book: Book):
    try:
        book_id = odoo.env['book_model'].create({
            'name': book.name,
            'author': book.author,
            'published_date': book.published_date,
            'isbn': book.isbn
        })
        return {"id": book_id, "message": "Book created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


#This endpoint return one book according to his id
@app.get("/api/books/{book_id}")
def show_book(book_id: int, lan: str | None):
    if lan is None:
        lan = "eng"

    try:
        book = odoo.env['book_model'].browse(book_id)
        if not book.exists():
            raise HTTPException(status_code=404, detail=errors_dict[10][lan])
        return {
            "name": book.name,
            "author": book.author,
            "published_date": book.published_date,
            "isbn": book.isbn
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


#This endpoint return all books in the database
@app.get("/api/books")
def show_books():
    try:
        books = odoo.env['book_model'].search_read([], ['name', 'author', 'published_date', 'isbn'])
        return books
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


#This endpoint update one data book according to his id and a book instance in the request body
@app.put("/api/books/{book_id}")
def update_book(book_id: int, book: Book):
    try:
        book_record = odoo.env['book_model'].browse(book_id)
        if not book_record.exists():
            raise HTTPException(status_code=404, detail="Book not found")

        book_record.write({
            'name': book.name,
            'author': book.author,
            'published_date': book.published_date,
            'isbn': book.isbn
        })

        return {"message": "Book updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


#This endpoint delete one book according to his id
@app.delete("/api/books/{book_id}")
def delete_book(book_id: int):
    try:
        book_record = odoo.env['book_model'].browse(book_id)
        if not book_record.exists():
            raise HTTPException(status_code=404, detail="Book not found")

        book_record.unlink()

        return {"message": "Book deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
