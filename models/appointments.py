# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import api
from odoo import fields
from odoo import models

class appointment(models.Model):
    
    _name = "aether.appointments"
    
    name = fields.Char(required=True)
    
    appointmentChange = fields.Boolean(string="AppointmentChange", required=True)
    
    appointmentDate = fields.Date(string="AppointmentDate", required=True)
    
    patient = fields.Many2one('res.users', ondelete='cascade', string="Patient", required=True)
    
    psychologist = fields.Many2one('res.users', ondelete='cascade', string="Psychologist", required=True)
 
 
    @api.onchange('Date', 'appointmentDate')
    def _verify_Available_Dates(self):
        if self.Date < today:
            return {'warning': {
                'title': "Incorrect 'Date' value", 
                'message': "The Date is not available today.", },
            }
            
            if self.Date < len(self.appointmentDate):
                return {'warning': {
                'title': "Too Many Dates", 
                'message': "Please Change Date", },
            }
            
            
            