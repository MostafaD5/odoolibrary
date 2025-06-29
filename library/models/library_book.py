from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    title = fields.Char(string="Title", required=True)
    _rec_name = 'title'
    author = fields.Char(required=True)
    isbn = fields.Char(string="ISBN")
    publication_year = fields.Integer()
    status = fields.Selection([
        ('available', 'Available'),
        ('borrowed', 'Borrowed')
    ])
    description = fields.Text()

    order_count = fields.Integer(string="Order Count", compute="_compute_order_count")

    @api.constrains('isbn')
    def _check_isbn(self):
        for record in self:
            if record.isbn:
                isbn = record.isbn.replace('-', '').replace(' ', '')
                if not isbn.isdigit():
                    raise ValidationError("ISBN يجب أن يحتوي على أرقام فقط.")
                if len(isbn) not in (10, 13):
                    raise ValidationError("ISBN يجب أن يكون 10 أو 13 رقم.")

    def _compute_order_count(self):
        for record in self:
            record.order_count = 0

    def action_view_orders(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Orders',
            'res_model': 'sale.order',
            'view_mode': 'tree,form',
            'domain': [('book_id', '=', self.id)],
            'context': {'default_book_id': self.id}
        }
