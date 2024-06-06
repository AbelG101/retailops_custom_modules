{
    'name': 'Shift Management',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Manage Employee Shifts and Shift Change Requests',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/shift_views.xml',
        'views/shift_request_views.xml',
    ],
    'installable': True,
    'application': True,
}
