# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import api
from odoo import fields
from odoo import models

class appointment(models.Model):
    _name = "aether.appointments"
    name = fields.Char(required=True)
    appointmentChange = fields.Boolean(string="Appointment change", required=True)
    appointmentDate = fields.Date(string="Appointment date", required=True)
    patient = fields.Many2one('res.users', ondelete='cascade', string="Patient", required=True)
    psychologist = fields.Many2one('res.users', ondelete='cascade', string="Psychologist", required=True)
    
    #Modify the application so that an Appointment can have many "Daily Notes" and a "Daily Notes" 
    #can be in many Appointments (Many to many)
    dailynote = fields.Many2many('aether.dailynote', ondelete='cascade', string="dailynote", required=True)
    
    
    
   

 