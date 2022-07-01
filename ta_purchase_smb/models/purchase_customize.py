import odoo.exceptions
from odoo import models, fields,api

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    x_size = fields.Char(string="Size")
    x_color = fields.Char(string="Color")
    x_small = fields.Float(string="Small", default=1.0, readonly=False)
    is_true = fields.Boolean(string="Is True", default=False)
    x_medium = fields.Float(string="Medium")
    x_large = fields.Float(string="Large")
    x_xlarge = fields.Float(string="X Large")
    x_36 = fields.Float(string="36")
    x_37 = fields.Float(string="37")
    x_38 = fields.Float(string="38")
    x_39 = fields.Float(string="39")
    x_40 = fields.Float(string="40")