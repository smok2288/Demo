from odoo import models, fields


class Partner(models.Model):
    _inherit = 'res.partner'

    message = fields.Char(string='Message')