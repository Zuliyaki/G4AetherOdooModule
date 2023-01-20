# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import api
from odoo import fields
from odoo import models

class dailynote(models.Model):
    _name = 'aether.dailynote'
    dnPatient = fields.Many2one('res.users', string="Patient", required=True)
    dnNoteText = fields.Text(string="Text", required=True)
    dnNoteComment = fields.Text(string="Comment")
    dnNoteStatus = fields.Selection([('READED', 'Readed'),
                                    ('NOTREADED', 'Not readed')], string="Status")
    dnNoteDate = fields.Date(string="Date", required=True)
    dnNoteDateLastEdited = fields.Date(string="Edit date")
    dnDayScore = fields.Float(string="Score", required=True)
    dnNoteReadable = fields.Boolean(string="Readable")