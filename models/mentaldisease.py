# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class mentaldisease(models.Model):
    _name = 'aether.mentaldisease'
    
    name = fields.Char(required=True)
    
    admin_ids = fields.Many2one('res.users', string="Admin", required=True)

    enum_mental_disease = fields.Selection([('MENTALILLNESS', 'Mental illness'), ('MENTALDISORDER', 'Mental disorder')], string="Type", required=True)
    
    description = fields.Text(string="Description", required=True)
    
    sympton = fields.Text(string="Sympton", required=True)
    
    add_date = fields.Date(string="Date", required=True)
    
    diagnosis_ids = fields.One2many('aether.diagnosis', 'mentalDisease', string="Diagnosis")

    