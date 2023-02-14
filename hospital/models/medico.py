from odoo import models, fields

class Medico(models.Model):
    _name = 'hospital.medico'
    _description = 'Medico'
    _rec_name = 'nombre'

    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellido/s', required=True)
    numeroColegiado = fields.Char('Numero de colegiado', required=True)