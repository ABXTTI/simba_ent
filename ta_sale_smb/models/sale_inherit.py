import odoo.exceptions
from odoo import models, fields,api

class SaleOrder(models.Model):
    _inherit = "sale.order"


    def write(self, vals):
        rtn = super(SaleOrder, self).write(vals)
        order_line = self.order_line
        total_advance = 0
        commission = 0
        for rec in order_line:
            if rec.product_id.is_advance_product:
                total_advance += (rec.product_uom_qty * rec.price_unit * rec.advance_in_percentage)
                if total_advance and self.partner_id.default_advance_in_percentage and self.partner_id.default_commission_percentage:
                    commission = total_advance * self.partner_id.default_commission_percentage
                    commission_product_id = self.env['product.template'].search([('name', '=', 'Commission'),('is_commission_product', '=', True)])
                    if len(commission_product_id) > 1:
                        raise odoo.exceptions.ValidationError("Commission Product Cannot be more than one !!!!!!!")
                    elif not commission_product_id:
                        raise odoo.exceptions.ValidationError("Create 1 Commission Product !!!!!")
        return rtn

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    advance_in_percentage = fields.Float(string="Advance in %")
    commission_percentage = fields.Float(string="Commission in %")

    @api.onchange('product_id')
    def get_values_onchange_product(self):
        for rec in self:
            if rec.product_id.is_commission_product:
                rec.commission_percentage = rec.order_partner_id.default_commission_percentage
            if rec.product_id.is_advance_product:
                rec.advance_in_percentage = rec.order_partner_id.default_advance_in_percentage