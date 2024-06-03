from odoo import models, fields, api

class ShelfLocation(models.Model):
    _name = 'shelf.location'
    _description = 'Shelf Location'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    capacity = fields.Float(string='Capacity')
    product_ids = fields.Many2many('product.product', string='Products')

    product_template_ids = fields.One2many('product.template', 'shelf_location_id', string='Products on Shelf')

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    shelf_location_id = fields.Many2one('shelf.location', string='Shelf Location')
    shelf_quantity = fields.Integer(string='Quantity on Shelf')
