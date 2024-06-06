# email_integration/__manifest__.py
{
    'name': 'Email Integration',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Module for sending emails from Odoo',
    'description': """
    Custom module to send emails from Odoo.
    """,
    'author': 'Abel G.',
    'depends': ['base', 'hr' ,'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_employee_email_view.xml',
        'data/email_template.xml',
    ],
    'installable': True,
    'application': True,
}
