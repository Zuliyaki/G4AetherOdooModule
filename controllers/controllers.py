# -*- coding: utf-8 -*-
from odoo import http

# class Aether(http.Controller):
#     @http.route('/aether/aether/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aether/aether/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aether.listing', {
#             'root': '/aether/aether',
#             'objects': http.request.env['aether.aether'].search([]),
#         })

#     @http.route('/aether/aether/objects/<model("aether.aether"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aether.object', {
#             'object': obj
#         })