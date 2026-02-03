# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Category(models.Model):
     _name = 'rentcars.category'
     _description = 'Category of vehicle'
     _parent_store = True

     active=fields.Boolean("Actif ?", default=True)
     name = fields.Char("Name")
     description= fields.Char("Description")

     vehicle_ids = fields.Many2many(
          "rentcars.vehicle",
          string="Vehicle With catégory"
     )
     parent_id = fields.Many2one(
          "rentcars.category",
          "Parent Category",
          ondelete="restrict")
     parent_path = fields.Char(index=True)

     # Optionnel, mais utile:
     child_ids = fields.One2many(
          "rentcars.category",
          "parent_id",
          "Subcategories")





