from odoo import api
from odoo import fields
from odoo import models

class psychologist(models.Model):
    _inherit = 'res.users'
    
    diagnosis=fields.OneToMany('aether.diagnosis','psychologist',String="Diagnosises")
    patient = fields.OneToMany('aether.patient', 'psychologist', String="Patients")