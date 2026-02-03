# -*- coding: utf-8 -*-
from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta
from pprint import pprint
class Vehicle(models.Model):
     # ---------------------------------------- Private Attributes ---------------------------------
     _name = 'rentcars.vehicle'
     _description = 'Description of vehicle'
     _rec_name="model"
     # --------------------------------------- Fields Declaration ----------------------------------
     active=fields.Boolean("Actif ?", default=True)
     immatriculation = fields.Char("Numberplate")
     date_purchased = fields.Date(string="Purchase date")
     model = fields.Char("Model")
     thumbnail = fields.Binary("Thumbnail")
     repairing_status=fields.Selection([
          ('arrived', 'Just arrived'),
          ('diagnoses','Diagnosing'),
          ('waiting', 'Waiting for parts'),
          ('repairing', 'Repairing'),
          ('finish', 'Finish')
     ], string="Repairing status", default='arrived', group_expand='_group_expand_states')

     kanban_state=fields.Selection([
        ('blocked', 'Blocked'),
        ('work', 'En cours')], string='Kanban State', default="work")

     repairing_priority=fields.Selection([
          ('0', 'Low'),
          ('1', 'Medium'),
          ('2', 'High'),
          ('3', 'Very High'),
     ])

     state=fields.Selection([('broken', 'Broken Down'), ('repaired', 'Being repaired'), ('usable', 'Usable')])
     # Computed
     age_vehicle=fields.Integer(compute="_age_vehicle", string="Age of vehicle (years)" , store=True)

     # Relational
     garage_id = fields.Many2one("rentcars.garage", string="Garage")

     # related
     garage_city=fields.Char(related="garage_id.address_city", string="Garage's city")

     option_ids = fields.Many2many(
         "rentcars.option",
         string="Option of vehicle"
     )

     category_ids = fields.Many2many(
          "rentcars.category",
          string="Category of vehicle"
     )

     booking_ids = fields.One2many(
          "rentcars.booking",
          "vehicle_id",
          string="booked vehicle")


     def _check_immatriculation(self) :
          self.ensure_one() #vérifie que quel self contient 1 seul record.
          pattern = re.compile("^\w{2}[0-9]{3}\w{2}$")
          return pattern.match(self.immatriculation)

     def _group_expand_states(self, states, domain, order):
          return [key for key, val in type(self).repairing_status.selection]

     def button_check_immatriculation(self):
          for vehicle in self:
               if not vehicle.immatriculation:
                    raise (ValidationError("Please provide an Numberplate for this car"))
               if vehicle.immatriculation and not vehicle._check_immatriculation():

                    raise ValidationError("%s Numberplate is invalid" % (vehicle.immatriculation)) #comment utilser la concatenation avec python https://www.geeksforgeeks.org/what-does-s-mean-in-a-python-format-string/
          return True



     @api.depends('date_purchased')
     def _age_vehicle(self):

          for vehicle in self:
               TODAY = date.today()
               vehicle.age_vehicle=relativedelta(TODAY, vehicle.date_purchased).years

     def test(self):
          isbn = 9782091648477
          total = 0
          digits = [int(x) for x in str(isbn)]
          if len(digits) == 13:
               for index, digit in enumerate(digits[:12]):
                    if (index % 2) == 0:
                         total += digit
                    else:
                         total += digit * 3

          reste = total % 10
          cleTheorique = 10 - reste if reste != 0 else 0
          resultat = digits[-1] == cleTheorique