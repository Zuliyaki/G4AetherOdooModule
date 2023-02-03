from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError

class mentaldisease(models.Model):
    _name = 'aether.mentaldisease'
    
    name = fields.Char(required=True)
    
    admin_ids = fields.Many2one('res.users', string="Admin", required=True)

    enum_mental_disease = fields.Selection([('MENTALILLNESS', 'Mental illness'), ('MENTALDISORDER', 'Mental disorder')], string="Type", default='MENTALILLNESS', required=True)
    
    description = fields.Text(string="Description", required=True)
    
    sympton = fields.Text(string="Sympton", required=True)
    
    add_date = fields.Date(string="Date", default=fields.Date.from_string(fields.Date.today()), required=True)
    
    diagnosis_ids = fields.One2many('aether.diagnosis', 'mentalDisease', string="Diagnosis")
  
    @api.constrains('add_date')
    def _constrains_date(self):
        for task in self:
            if fields.Date.from_string(task.add_date) > fields.Date.from_string(fields.Date.today()):
                raise exceptions.ValidationError("Date cannot be greater than today date.")
            
    @api.onchange('add_date')
    def _onchange_date(self):
        if fields.Date.from_string(self.add_date) > fields.Date.from_string(fields.Date.today()):
            return{
                'warning':{
                    'title': "Date incorrect",
                    'message': "Date cannot be greater than today date.",
                },
            }