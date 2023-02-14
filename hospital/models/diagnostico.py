# -*- coding: utf-8 -*-
from odoo import models, fields

class Diagnostico(models.Model):
    _name = 'hospital.diagnostico'
    _description = "Diagnostico"

    _rec_name = 'id'

    paciente = fields.Many2one('hospital.paciente', string="Paciente", required=True)
    medico = fields.Many2one('hospital.medico',string='Medico', required=True)
    diagnostico = fields.Text('Diagnostico', required=True)
