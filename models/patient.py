from odoo import api
from odoo import fields
from odoo import models

class patient(models.Model):
    _inherit = 'res.users'
    
    diagnosis = fields.One2many('aether.diagnosis', 'patient', string="Diagnosis")
    dailynote = fields.One2many('aether.dailynote', 'dnPatient', string="Daily Note")
    # psychologist = fields.Many2one('aether.psychologist', ondelete='cascade', string="Psychologist", required=True)
    appointment = fields.One2many('aether.appointments', 'patient', string ="Appointment")
    