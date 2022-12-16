# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class mentaldisease(models.Model):
    _name = 'aether.mentaldisease'

    admin_id = fields.Many2one('res.users', ondelete='set null', string="Admin", required=True)
    
    enum_mental_disease = fields.Selection([('mentalillness', 'Mental illness'), ('mentaldisorder', 'Mental disorder')], required=True)
    
    name = fields.Char(string="Name", required=True)
    
    description = fields.Text(string="Description", required=True)
    
    sympton = fields.Text(string="Sympton", required=True)
    
    add_date = fields.DateTime(string="Add date", required=True)
    
    diagnosis_ids = fields.One2many('aether.diagnosis', 'mentalDisease', string="Diagnosis")

    