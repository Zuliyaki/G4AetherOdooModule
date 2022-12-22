# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import fields
from odoo import models

class DailyNote(models.Model):
    _name = 'aether.dailynote'
    dnPatient = Many2One('aether.patient', string="Patient", required=True)
    dnNoteText = fields.Text(string="Text", required=True)
    dnNoteComment = fields.Text(string="Comment")
    dnNoteStatus = fields.Selection([('READED', 'READED'),
                                    ('NOTREADED', 'NOTREADED')], string="Status")
    dnNoteDate = fields.Date(string="Date")
    dnNoteDateLastEdited = fields.Date(string="Edit date")
    dnDayScore = fields.Float(string="Score", required=True)
    dnNnoteReadable = fields.Boolean(string="Readable")