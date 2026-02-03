# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Option(models.Model):
     _name = 'rentcars.option'
     _description = 'Options of vehicle'
     active=fields.Boolean("Actif ?", default=True)
     name = fields.Char("Name")
     category = fields.Selection([("security", "security"), ("comfort", "comfort"), ("aestheticism", "aestheticism")])
     description= fields.Char("Description")

     vehicle_ids = fields.Many2many(
          "rentcars.vehicle",
          string="Vehicle With option"
     )






