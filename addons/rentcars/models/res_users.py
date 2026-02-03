# -*- coding: utf-8 -*-

from odoo import fields, models


class ResUsers(models.Model):

    # ---------------------------------------- Private Attributes ---------------------------------

    # _inherit = "res.users"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Relational
    booking_ids = fields.One2many(
        "rentcars.booking", "user_id", string="Booking"
    )