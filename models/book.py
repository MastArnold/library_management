from odoo import models, fields


class Book(models.Model):
    _name = 'book_model'
    _description = 'Book'

    name = fields.Char(string='Name', required=True)
    author = fields.Char(string='Author', required=True)
    published_date = fields.Date(string='Published Date')
    isbn = fields.Char(string='ISBN')
