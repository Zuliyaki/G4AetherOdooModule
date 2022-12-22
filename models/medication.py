# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


from odoo import api
from odoo import fields
from odoo import models

#class medication(models.Model):
 #   _name = 'aether.medication'
 #   
 #   name = fields.Char(required=True)
 #   description = fields.Text(required=True)
 #   medicationType = fields.Selection([('ANTIDEPRESSANTS', 'ANTIDEPRESSANTS'), ('ANTIANXIETYMEDICATIONS', 'ANTI ANXIETY MEDICATIONS'),
 #                                     ('STIMULANTS', 'STIMULANTS'), ('ANTIPSYCHOTICS', 'ANTI PSYCHOTICS'), ('MOODSTABILIZERS', 'MOOD STABILIZERS')], required=True)
 #   treatment = fields.OneToMany('aether.treatment', 'medication', String="treatments")