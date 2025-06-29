from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_library_member = fields.Boolean(string="Library Member")

    loan_ids = fields.One2many(
        comodel_name='library.loan',
        inverse_name='partner_id',
        string="Library Loans"
    )

    loan_count = fields.Integer(
        string="Loan Count",
        compute='_compute_loan_count'
    )

    @api.depends('loan_ids')
    def _compute_loan_count(self):
        for partner in self:
            partner.loan_count = len(partner.loan_ids)
