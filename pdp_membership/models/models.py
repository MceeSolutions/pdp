# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'

    code = fields.Char(string='code', readonly=True, copy=False, default='New')
    ward_id = fields.Many2one(comodel_name='lga.ward', string='Ward', required=True)

    def generate_code(self):
        self.code =  self.ward_id.lga_id.state_id.code + '/' + self.ward_id.lga_id.code + '/' + self.ward_id.code + '/' + self.env['ir.sequence'].next_by_code('lga.ward') or '/'

    @api.model
    def create(self, vals):
        res = super(Partner, self).create(vals)
        res.generate_code()
        return res 

class LGA(models.Model):
    _name = 'state.lga'

    name = fields.Char(string='Name')
    state_id = fields.Many2one(comodel_name='res.country.state', string='Name')
    code = fields.Char(string='Code')

class LGA(models.Model):
    _name = 'lga.ward'

    name = fields.Char(string='Name')
    lga_id = fields.Many2one(comodel_name='state.lga', string='Name')
    code = fields.Char(string='Code')


# class pdp_membership(models.Model):
#     _name = 'pdp_membership.pdp_membership'
#     _description = 'pdp_membership.pdp_membership'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
