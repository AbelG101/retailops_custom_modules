{
    'name': 'Shelf Space Management',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Manage and optimize shelf space in a supermarket',
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        'views/shelf_space_views.xml',
        'views/shelf_space_menu.xml',
    ],
    'installable': True,
    'application': True,
}
