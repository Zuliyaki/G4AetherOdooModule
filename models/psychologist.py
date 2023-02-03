from odoo import api
from odoo import fields
from odoo import models

class psychologist(models.Model):
    _inherit = 'res.users'
    
    diagnosis_id = fields.One2many('aether.diagnosis','psychologist', string="Diagnosises")
    # patient_id = fields.One2many('aether.patient', 'psychologist', string="Patients")
    appointment = fields.One2many('aether.appointments', 'psychologist', string="Appointments")