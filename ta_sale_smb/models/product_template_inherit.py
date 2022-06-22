from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_commission_product = fields.Boolean(string="Is Commission Product:")
    is_advance_product = fields.Boolean(string="Is Advance Product")
