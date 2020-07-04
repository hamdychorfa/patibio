from odoo import fields, api, models


class MrpLocation(models.Model):
    _name = "mrp.location"
    _description = "manufacturing location"

    name = fields.Char(string="Manufacturing location")


