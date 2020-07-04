from odoo import fields, api, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    status_manufacturing = fields.Selection([('production', 'En production'), ('stopped', 'Arrêté')], string='Etat',
                                  default='stopped')
    location_manufacturing = fields.Many2one('mrp.location', string='Lieu de fabrication')

    def product_sheet_report(self):
        return

    def technical_sheet_report(self):
        return
