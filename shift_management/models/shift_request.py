from odoo import models, fields, api

class ShiftRequest(models.Model):
    _name = 'shift.management.shift.request'
    _description = 'Shift Change Request'
    _inherit =  ['mail.thread', 'mail.activity.mixin']

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, tracking = True)
    current_shift_id = fields.Many2one('shift.management.shift', string='Current Shift', required=True, tracking = True)
    requested_shift_id = fields.Many2one('shift.management.shift', string='Requested Shift', required=True, tracking = True)
    reason = fields.Text(string='Reason', tracking = True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('denied', 'Denied')
    ], string='Status', default='draft', tracking = True)

    @api.model
    def create(self, vals):
        request = super(ShiftRequest, self).create(vals)
        request.message_post(body="Shift change request created.")
        
        return request

    def action_approve(self):
        for record in self:
            record.state = 'approved'
            record.current_shift_id.employee_ids = [(3, record.employee_id.id)]
            record.requested_shift_id.employee_ids = [(4, record.employee_id.id)]
            record.message_post(body="Shift change request approved.")

    def action_deny(self):
        for record in self:
            record.state = 'denied'
            record.message_post(body="Shift change request denied.")
