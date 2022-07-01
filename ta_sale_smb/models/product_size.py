from odoo import models, fields


class ProductSize(models.Model):
    _name = "product.size"

    name = fields.Char(string="Product Size")
