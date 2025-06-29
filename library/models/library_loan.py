from odoo import models, fields, api
from datetime import datetime, date, time
from odoo.exceptions import ValidationError

class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Library Loan'
    _rec_name = 'book_id'

    book_id = fields.Many2one('library.book', string='Book', required=True)
    partner_id = fields.Many2one('res.partner', string='Member', required=True)
    borrow_date = fields.Datetime(string='Borrow Date', default=fields.Datetime.now)
    return_date = fields.Datetime(string='Return Date')
    status = fields.Selection([
        ('active', 'Active'),
        ('returned', 'Returned'),
    ], string="Status", default='active')

    def action_return_book(self):
        for record in self:
            if record.status != 'returned':
                record.status = 'returned'
                record.book_id.status = 'available'

    @api.constrains('book_id')
    def _check_book_available(self):
        for record in self:
            if record.book_id.status == 'borrowed' and record.status == 'active':
                raise ValidationError("This book is already borrowed.")

    @api.model
    def create(self, vals):
        record = super().create(vals)
        if record.status == 'active':
            record.book_id.status = 'borrowed'
        return record

    def write(self, vals):
        res = super().write(vals)
        for record in self:
            if record.status == 'returned':
                record.book_id.status = 'available'
        return res
