from odoo import models, fields

class Paciente(models.Model):
    _name = 'hospital.paciente'
    _description = 'Paciente'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellido/s', required=True)
    sintomas = fields.Char(string='Sintomas')