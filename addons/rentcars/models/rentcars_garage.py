# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Garage(models.Model):
     _name = 'rentcars.garage'
     _description = 'A garage is a location for vehicle'
     name = fields.Char("Name")
     active=fields.Boolean("Actif ?", default=True)
     address_street = fields.Char("Street")
     address_zipcode = fields.Char("Zip code")
     address_city = fields.Char("City")
     places_max = fields.Integer("No. of places")
     vehicle_ids = fields.One2many(
          "rentcars.vehicle",
          "garage_id",
          string="parked vehicles")
     user_id = fields.Many2one("res.users", string="Responsable", default=lambda self: self.env.user)




