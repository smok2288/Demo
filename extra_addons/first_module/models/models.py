import quantity as quantity
from odoo import models, fields, api



class Warehouse(models.Model):
    _name = 'first_module.warehouse'

    name = fields.Char(string='Title')
    quantity = fields.Integer(string='quantity')
    description = fields.Char(string='description')
    price = fields.Integer(string='price')
    manufacturer_ids = fields.Many2many('first_module.manufacturer', string='manufacturer')
    status = fields.Selection([('new', 'New'), ('used', 'Used')], string='Status', default='new')
    zap_ids = fields.One2many('first_module.zap', 'name', string='Zaps')


class Zap(models.Model):
    _name = 'first_module.zap'

    name = fields.Many2one('first_module.warehouse', string='Title')
    price = fields.Integer(string='price', compute='get_first_price')
    quantity = fields.Integer(string='quantity')
    buyer_id = fields.Many2one('res.partner', string='Buyer')
    car_id = fields.Many2one('first_module.car', string='Car')
    total_price = fields.Integer(string='total price', compute='get_price')
    zap_sequence = fields.Char(string='sequence')

    def get_first_price(self):
        self.price = self.name.price

    def get_price(self):
        self.total_price = self.price*self.quantity*1.2

    def set_zap_used(self):
        self.status = 'used'

    def set_zap_new(self):
        self.status = 'new'



    @api.model
    def create(self, vals):
        vals['zap_sequence'] = self.env['ir.sequence'].next_by_code('zap.sequence')
        result = super(Zap, self).create(vals)
        return result

class Car(models.Model):
    _name = 'first_module.car'

    name = fields.Char(string='name')
    zap_ids = fields.One2many('first_module.zap', 'car_id', string='Zaps')

class Manufacturer(models.Model):
    _name = 'first_module.manufacturer'

    name = fields.Char(string='Brand')
    country = fields.Char(string='Country')



# class first_module(models.Model):
#     _name = 'first_module.first_module'
#     _description = 'first_module.first_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
