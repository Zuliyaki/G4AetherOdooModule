from odoo import api
from odoo import fields
from odoo import models

class patient(models.Model):
    _inherit = 'res.users'
    
    diagnosis = fields.OneToMany('aether.diagnosis', 'patient', String="Diagnosis")
    dailynote = fields.OneToMany('aether.dailynote', 'dnPatient', String="Daily Note")
    psychologist = fields.Many2one('res.users', ondelete='cascade',
                              string="Psychologist", required=True)
    
    