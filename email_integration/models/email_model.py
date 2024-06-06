from odoo import models, fields

class Employee(models.Model):
    _inherit = 'hr.employee'
    _description = 'Email Model'

    email_body = fields.Html(string="Email Body")
    email_subject = fields.Char(string="Email Subject")

    def action_send_mail(self):
        template = self.env.ref('email_integration.email_template')
        self.ensure_one()
        context = {
            'email_body': self.email_body,
            'email_subject': self.email_subject,
        }
        template.with_context(context).send_mail(self.id, force_send=True)
