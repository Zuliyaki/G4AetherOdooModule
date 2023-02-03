# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import api
from odoo import fields
from odoo import models

class admin(models.Model):
    _inherit = 'res.users'
    
    mentaldisease_ids = fields.One2many('aether.mentaldisease', 'admin_ids', string="MentalDisease")
