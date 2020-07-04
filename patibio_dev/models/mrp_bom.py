from odoo import fields, api, models


class MrpBom(models.Model):
    _inherit = "mrp.bom"

    location_manufacturing = fields.Many2one('mrp.location', string='Lieu de fabrication')

    tags = fields.Many2one('mrp.tags', string='Type étiquette')
    can_be_frozen = fields.Boolean(string='Peut être congelé')
    lot_manufacturing = fields.Boolean(string='Lot de fabrication ')
    dlv = fields.Char(string='DLV')
    dlc = fields.Char(string='DLC')
    dluo = fields.Char(string='DLUO ')

    #####
    selled_by = fields.Char(string='Vendu par ')
    #####

    weight_product = fields.Char(string='Poids produit')
    informations_conserve = fields.Text(string='Info. de conservation: ')
