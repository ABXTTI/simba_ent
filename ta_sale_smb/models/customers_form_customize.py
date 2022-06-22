from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    default_advance_in_percentage = fields.Float(string="Advance in (%)")
    default_commission_percentage = fields.Float(string="Default Commission (%)")



