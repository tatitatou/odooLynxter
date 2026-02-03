# -*- coding: utf-8 -*-

from odoo import http

class Vehicles(http.Controller):
    @http.route("/rentcars/vehicles")

    def list(self, **kwargs) :
        Vehicle=http.request.env["rentcars.vehicle"]
        vehicles=Vehicle.search([])
        return http.request.render(
            "rentcars.vehicle_list_template",
            {"vehicles":vehicles}
        )

    @http.route("/rentcars/vehicle/<model('rentcars.vehicle'):vehicle>")
    def detail(self, vehicle):
        return http.request.render(
            "rentcars.vehicle_detail_template",
            {"vehicle": vehicle}
        )

