# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Booking(models.Model):


     # ---------------------------------------- Private Attributes ---------------------------------
     _name = 'rentcars.booking'
     _description = 'Réservation d\'un véhicule par un user'
     _inherit = ['mail.thread', 'mail.activity.mixin']
     # --------------------------------------- Fields Declaration ----------------------------------

     # Basic
     active=fields.Boolean("Actif ?", default=True)
     date_start = fields.Datetime("Start of booking")
     date_delay = fields.Float("duree")

     # Relational
     vehicle_id = fields.Many2one("rentcars.vehicle", string="Vehicule")
     vehicle_model=fields.Char(related='vehicle_id.model')
     vehicle_date_purchased=fields.Char(related='vehicle_id.immatriculation')

     user_id = fields.Many2one("res.users", string="Utilisateur", default=lambda self: self.env.user)
     user_name=fields.Char(related='user_id.name')

     # ----------------------------------------  methods ------------------------------------
     def _compute_display_name(self):    
          for rec in self:
               rec.display_name = f"{rec.vehicle_id.model} - {rec.user_name}"



