from odoo import models, fields, api
from odoo.exceptions import UserError


class BookBorrowWizard(models.TransientModel):
    _name = 'book.borrow.wizard'
    _description = 'Wizard to Borrow Book'

    member_id = fields.Many2one('res.partner', string="Member", required=True,
                                domain="[('is_library_member','=',True)]")
    book_id = fields.Many2one('library.book', string="Book", required=True)

    def action_borrow_book(self):
        # make sure book is avalabile
        if self.book_id.available_qty < 1:
            raise UserError("This book is not available for borrowing.")

        # create loan
        self.env['library.loan'].create({
            'book_id': self.book_id.id,
            'partner_id': self.member_id.id,
        })
