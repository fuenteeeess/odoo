from odoo import models, fields

class Profesor(models.Model):
    _name = 'ciclos.profesor'
    _description = 'Profesor'
    _rec_name = 'nombre'

    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellido/s')