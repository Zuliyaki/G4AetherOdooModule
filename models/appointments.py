# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#from odoo import api
from odoo import fields
from odoo import models

class Appointment(models.Model):
    _name = "aether.appointments"
    
    appointmentChange = fields.Boolean()(string="appointmentChange", required=True)
    appointmentDate = fields.date()(string="appointmentDate", required=True)
    patient = fields.Many2one('res.users', ondelete='cascade', string="Patient", required=True)
    psychologist = fields.Many2one('res.users', ondelete='cascade', string="Psychologist", required=True)
  