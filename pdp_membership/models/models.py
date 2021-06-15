# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'

    code = fields.Char(string='code', readonly=True, copy=False, default='New')
    ward_id = fields.Many2one(comodel_name='lga.ward', string='Ward')
    state_id = fields.Many2one(comodel_name='res.country.state', string='State')
    lga_id = fields.Many2one(comodel_name='state.lga', string='Lga')

    def generate_code(self):
        self.code =  self.state_id.code + '/' + self.lga_id.code + '/' + self.ward_id.code + '/' + self.env['ir.sequence'].next_by_code('lga.ward') or '/'

    @api.model
    def create(self, vals):
        res = super(Partner, self).create(vals)
        res.generate_code()
        return res 

    @api.onchange('ward_id')
    def ward_id_change(self):
        if self.ward_id:
            self.lga_id = self.ward_id.lga_id
            self.state_id = self.ward_id.lga_id.state_id


class LGA(models.Model):
    _name = 'state.lga'
    _description = 'LGA'

    name = fields.Char(string='Name', required=True)
    state_id = fields.Many2one(comodel_name='res.country.state', string='State')
    code = fields.Char(string='Code', required=True)

class Ward(models.Model):
    _name = 'lga.ward'
    _description = 'Ward'

    name = fields.Char(string='Name', required=True)
    lga_id = fields.Many2one(comodel_name='state.lga', string='Lga')
    code = fields.Char(string='Code', required=True)


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
