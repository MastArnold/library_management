from odoo import http
from odoo.http import request


class LibraryBookController(http.Controller):

    @http.route('/library/book/delete/<int:book_id>', type='http', auth='user', methods=['POST'], csrf=False)
    def delete_book(self, book_id, **kwargs):
        book = request.env['book_model'].browse(book_id)
        if book.exists():
            book.unlink()
            return "Book deleted successfully"
        return "Book not found"

    @http.route('/library/book/edit/<int:book_id>', type='http', auth='user', methods=['POST'], csrf=False)
    def edit_book(self, book_id, **kwargs):
        book = request.env['book_model'].browse(book_id)
        if book.exists():
            data = {
                'name': kwargs.get('name'),
                'author': kwargs.get('author'),
                'published_date': kwargs.get('published_date'),
                'isbn': kwargs.get('isbn')
            }
            book.write(data)
            return "Book updated successfully"
        return "Book not found"
