from odoo import models, fields

class Shift(models.Model):
    _name = 'shift.management.shift'
    _description = 'Shift'

    name = fields.Char(string='Shift Name', required=True)
    start_time = fields.Float(string='Start Time', required=True)
    end_time = fields.Float(string='End Time', required=True)
    employee_ids = fields.Many2many('hr.employee', string='Employees')
 