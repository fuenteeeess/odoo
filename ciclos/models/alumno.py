from odoo import models, fields

class Alumno(models.Model):
    _name = 'ciclos.alumno'
    _description = 'Alumno'
    _rec_name = 'nombre'

    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellido/s')