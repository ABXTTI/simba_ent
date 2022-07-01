import odoo.exceptions
from odoo import models, fields,api

class SaleOrder(models.Model):
    _inherit = "sale.order"


    def write(self, vals):
        rtn = super(SaleOrder, self).write(vals)
        order_line = self.order_line
        total_advance = 0
        commission = 0
        commission_product_id = self.env['product.template'].search(
            [('name', '=', 'Commission'), ('is_commission_product', '=', True)])
        for rec in order_line:
            if rec.product_id.is_advance_product:
                total_advance += (rec.product_uom_qty * rec.price_unit * ((1 - rec.advance_in_percentage / 100) if rec.advance_in_percentage else 1))

                if total_advance:
                    commission = total_advance * self.partner_id.default_commission_percentage / 100
                    if len(commission_product_id) > 1:
                        raise odoo.exceptions.ValidationError("Commission Product Cannot be more than one !!!!!!!")
                    elif not commission_product_id:
                        raise odoo.exceptions.ValidationError("Create 1 Commission Product !!!!!")


        commission_line_exist = order_line.search([('product_id', '=', commission_product_id.id),('order_id', '=', self.id)])
        if not commission_line_exist and commission:
            order_line.create({
                'product_id': commission_product_id.id,
                'commission_percentage': self.partner_id.default_commission_percentage,
                'product_uom_qty': 1,
                'price_unit': commission,
                'order_id': self.id,
            })
        return rtn

    @api.model
    def create(self, vals_list):
        rtn = super(SaleOrder, self).create(vals_list)
        order_line = rtn.order_line
        total_advance = 0
        commission = 0
        commission_product_id = self.env['product.template'].search(
            [('name', '=', 'Commission'), ('is_commission_product', '=', True)])
        for rec in order_line:
            if rec.product_id.is_advance_product:
                total_advance += (rec.product_uom_qty * rec.price_unit * ((1 - rec.advance_in_percentage / 100) if rec.advance_in_percentage else 1))

                if total_advance:
                    commission = total_advance * rtn.partner_id.default_commission_percentage / 100
                    if len(commission_product_id) > 1:
                        raise odoo.exceptions.ValidationError("Commission Product Cannot be more than one !!!!!!!")
                    elif not commission_product_id:
                        raise odoo.exceptions.ValidationError("Create 1 Commission Product !!!!!")

        commission_line_exist = order_line.search([('product_id', '=', commission_product_id.id),('order_id', '=', rtn.id)])
        if not commission_line_exist and commission:
            order_line.create({
                'product_id': commission_product_id.id,
                'commission_percentage': rtn.partner_id.default_commission_percentage,
                'product_uom_qty': 1,
                'price_unit': commission,
                'order_id': rtn.id,
            })
        return rtn

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    advance_in_percentage = fields.Float(string="Advance in %")
    commission_percentage = fields.Float(string="Commission in %")
    is_commission_product = fields.Boolean(string="IS Commission Product", related="product_id.is_commission_product")
    is_advance_product = fields.Boolean(string="IS Commission Product", related="product_id.is_advance_product")
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

    @api.onchange('product_id')
    def get_values_onchange_product(self):
        for rec in self:
            if rec.product_id.is_commission_product:
                rec.commission_percentage = rec.order_partner_id.default_commission_percentage
            elif rec.product_id.is_advance_product:
                rec.advance_in_percentage = rec.order_partner_id.default_advance_in_percentage

    @api.onchange('commission_percentage')
    def onchange_commission_percentage(self):
        for rec in self:
            total_advance = 0
            commission = 0
            if rec.product_id.is_commission_product:
                order_line = rec.order_id.order_line
                for line in order_line:
                    if line.product_id.is_advance_product:
                        total_advance += (line.product_uom_qty * line.price_unit * ((1 - line.advance_in_percentage / 100) if line.advance_in_percentage else 1))
                        if total_advance:
                            commission = total_advance * rec.commission_percentage / 100

                rec.price_unit = commission