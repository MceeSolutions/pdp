# -*- coding: utf-8 -*-
# from odoo import http


# class PdpMembership(http.Controller):
#     @http.route('/pdp_membership/pdp_membership/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pdp_membership/pdp_membership/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pdp_membership.listing', {
#             'root': '/pdp_membership/pdp_membership',
#             'objects': http.request.env['pdp_membership.pdp_membership'].search([]),
#         })

#     @http.route('/pdp_membership/pdp_membership/objects/<model("pdp_membership.pdp_membership"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pdp_membership.object', {
#             'object': obj
#         })
