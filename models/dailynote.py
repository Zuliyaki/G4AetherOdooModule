# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError

class dailynote(models.Model):
    _name = 'aether.dailynote'
    dnPatient = fields.Many2one('res.users', string="Patient", required=True)
    dnNoteText = fields.Text(string="Text", required=True)
    dnNoteComment = fields.Text(string="Comment", required=True)
    dnNoteStatus = fields.Selection([('Readed', 'READED'), ('NotReaded', 'NOTREADED')], string="Status", default='NotReaded')
    dnNoteDate = fields.Date(string="Date", required=True ,default=fields.Date.from_string(fields.Date.today()))
    dnNoteDateLastEdited = fields.Date(string="Edit date" ,default=fields.Date.from_string(fields.Date.today()))
    dnDayScore = fields.Float(string="Score", required=True, default=5)
    dnNoteReadable = fields.Boolean(string="Readable")
    
    # onchange handler for score
    @api.onchange('dnDayScore')
    def _onchange_score(self):
        if self.dnDayScore < 0 or self.dnDayScore > 10:
            return {
                'warning': {
                    'title': "Wrong score",
                    'message': "The content needs to be betwheen 0 and 10.",
                }
            }
    
    # onchange handler for date
    @api.onchange('dnNoteDate')
    def _onchange_date(self):
        if fields.Date.from_string(self.dnNoteDate) != fields.Date.from_string(fields.Date.today()):
            return {
                'warning': {
                    'title': "Wrong date",
                    'message': "Creating a new note must contain todays date, if you want to create another days date, check if the note date is not already inserted",
                }
            }

    @api.constrains('dnDayScore')
    def _check_score_between_0_and_10(self):
        for task in self:
            if task.dnDayScore < 0 or task.dnDayScore > 10:
                raise ValidationError("The content needs to be betwheen 0 and 10.")
            
    @api.constrains('dnDayScore')
    def _check_validation_on_date(self):
        for task in self:
            if fields.Date.from_string(task.dnNoteDate) > fields.Date.from_string(fields.Date.today()):
                raise ValidationError("Creating a note can not contain a date after todays date.")