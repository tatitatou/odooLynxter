# -*- coding: utf-8 -*-
# from odoo import http


# class Rentcars(http.Controller):
#     @http.route('/rentcars/rentcars', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rentcars/rentcars/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rentcars.listing', {
#             'root': '/rentcars/rentcars',
#             'objects': http.request.env['rentcars.rentcars'].search([]),
#         })

#     @http.route('/rentcars/rentcars/objects/<model("rentcars.rentcars"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rentcars.object', {
#             'object': obj
#         })
