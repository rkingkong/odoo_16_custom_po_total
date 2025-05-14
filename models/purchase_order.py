from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    x_total_with_tax = fields.Monetary(
        string='Total with Tax',
        compute='_compute_x_total_with_tax',
        store=True,
        currency_field='currency_id',
        help='Total amount including taxes and subtotal'
    )

    @api.depends('amount_untaxed', 'amount_tax')
    def _compute_x_total_with_tax(self):
        for order in self:
            order.x_total_with_tax = order.amount_untaxed + order.amount_tax

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    x_line_total_with_tax = fields.Monetary(
        string='Total with Tax',
        compute='_compute_x_line_total_with_tax',
        store=True,
        currency_field='currency_id',
        help='Line total including taxes'
    )

    @api.depends('price_subtotal', 'price_tax')
    def _compute_x_line_total_with_tax(self):
        for line in self:
            line.x_line_total_with_tax = line.price_subtotal + line.price_tax
