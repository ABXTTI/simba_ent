#############################################
###################################################################################

{
    'name': 'TA BASE',
    'summary': 'Odoo Community Backend Theme',
    'version': '15.0.1.0.1',
    'category': 'Other',
    'license': 'LGPL-3',
    'author': 'The Adepts',
    'website': 'http://www.ta.net',
    'contributors': [
        'Mathias Markl <mathias.markl@mukit.at>',
    ],
    'depends': ['base', 'sale', 'stock'],
    'excludes': [
        'web_enterprise',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_size.xml',
        'views/product_template_inherit.xml',
        'views/customers_form_inherit.xml',
        'views/sale_inherit.xml',
    ],
    'assets': {
        'web.assets_qweb': [],
        'web._assets_primary_variables': [],
        'web._assets_backend_helpers': [],
        'web.assets_backend': [],
    },
    'images': [],
    'external_dependencies': {
        'python': [],
        'bin': [],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'uninstall_hook': '_uninstall_reset_changes',
}
