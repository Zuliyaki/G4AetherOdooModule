# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError

class diagnosis(models.Model):
    _name = 'aether.diagnosis'
    
    name = fields.Char(required=True)
    diagnosisDate = fields.Date(required=True, default=fields.Date.from_string(fields.Date.today()))
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


    @api.constrains('lastDiagnosisChangeDate')
    def _check_validation_datecreation_not_after_modification(self):
        for task in self:
            if fields.Date.from_string(task.lastDiagnosisChangeDate) < fields.Date.from_string(task.diagnosisDate):
                raise ValidationError("the last diagnosis change cannot be greater than the creation one")

    @api.onchange('lastDiagnosisChangeDate')
    def _check_validation_datecreation_not_after_modificationOnFocusLost(self):
        if fields.Date.from_string(self.lastDiagnosisChangeDate) < fields.Date.from_string(self.diagnosisDate):
            return {
                'warning': {
                    'title': "Wrong Date",
                    'message': "the last diagnosis change cannot be greater than the creation one",
                }
            }
