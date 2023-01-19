from odoo import api
from odoo import fields
from odoo import models

class psychologist(models.Model):
    _inherit = 'res.users'
    
    #diagnosis=fields.One2many('aether.diagnosis','psychologist', string="Diagnosises")
    #patient = fields.One2many('res.users', 'psychologist', string="Patients")
    appointment = fields.One2many('aether.appointments', 'psychologist', string="Appointment")