# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class diagnosis(models.Model):
    _name = 'aether.diagnosis'
    
    name = fields.Char(required=True)
    diagnosisDate = fields.Date(required=True)
    lastDiagnosisChangeDate = fields.Date(required=True)
    patient = fields.Many2one('res.users', ondelete='cascade',
                              string="Patient", required=True)
    psychologist = fields.Many2one('res.users', ondelete='cascade',
                                   string="Psychologist", required=True)
    mentalDisease = fields.Many2one('aether.mentaldisease', ondelete='cascade',
                                    string="MentalDisease", required=True)
    onTherapy = fields.Boolean(string="Active", required=True)
    
    medicationType = fields.Selection([('ANTIDEPRESSANTS', 'ANTIDEPRESSANTS'), ('ANTIANXIETYMEDICATIONS', 'ANTI ANXIETY MEDICATIONS'),
                                      ('STIMULANTS', 'STIMULANTS'), ('ANTIPSYCHOTICS', 'ANTI PSYCHOTICS'), ('MOODSTABILIZERS', 'MOOD STABILIZERS')], required=True)
