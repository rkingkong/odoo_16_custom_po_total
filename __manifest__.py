
{
    'name': 'Custom Purchase Order Total',
    'version': '1.0',
    'category': 'Purchases',
    'summary': 'Add a column showing total (tax + subtotal) in purchase orders',
    'description': """
        This module adds a new computed field to purchase orders that displays the 
        total amount including taxes and subtotal.
    """,
    'author': 'Your Name',
    'depends': ['purchase'],
    'data': [
        'views/purchase_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
