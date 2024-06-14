from odoo import fields, models


class Book(models.Model):
    _name = "book_model"
    _description = "Book Model"

    name = fields.Char(string="Name", required=True)
    author = fields.Char(string="Author", required=True)
    published_date = fields.Date(string="Published_date")
    isbn = fields.Char(string="Isbn")

    def action_delete(self):
        for record in self:
            record.unlink()

    def action_save(self):
        for record in self:
            record.write(record._convert_to_write(record._cache))