from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'  # This might be different in Torelo

    x_total_with_tax = fields.Monetary(
        string='Total with Tax',
        compute='_compute_x_total_with_tax',
        store=True,
        currency_field='currency_id',  # Adjust if Torelo uses a different field
        help='Total amount including taxes and subtotal'
    )

    @api.depends('amount_untaxed', 'amount_tax')  # Adjust field names if needed
    def _compute_x_total_with_tax(self):
        for order in self:
            # Based on your screenshot, this might need to be adjusted
            # The field names might be different in Torelo
            order.x_total_with_tax = order.amount_untaxed + order.amount_tax

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'  # This might be different in Torelo

    x_line_total_with_tax = fields.Monetary(
        string='Total with Tax',
        compute='_compute_x_line_total_with_tax',
        store=True,
        currency_field='currency_id',  # Adjust if Torelo uses a different field
        help='Line total including taxes'
    )

    @api.depends('price_subtotal', 'price_tax')  # Adjust field names if needed
    def _compute_x_line_total_with_tax(self):
        for line in self:
            # From your screenshot, you might need to adapt these field names
            # For example, subtotal seems to be displayed with a $ sign
            line.x_line_total_with_tax = line.price_subtotal + line.price_tax
