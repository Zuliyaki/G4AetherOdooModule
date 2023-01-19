# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import api
from odoo import fields
from odoo import models

class Appointment(models.Model):
    _name = "aether.appointments"
    name = fields.Char(required=True)
    
    appointmentChange = fields.Boolean(string="AppointmentChange", required=True)
    appointmentDate = fields.Date(string="AppointmentDate", required=True)
    patient = fields.Many2one('res.users', string="Patient", required=True)
    psychologist = fields.Many2one('res.users', string="Psychologist", required=True)
 
