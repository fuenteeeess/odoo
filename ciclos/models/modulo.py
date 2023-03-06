from odoo import models, fields

class Modulo(models.Model):
    _name = 'ciclos.modulo'
    _description = 'Modulo'
    _rec_name = 'nombre'

    nombre = fields.Char('Nombre', required=True)
    profesor = fields.Many2one('ciclos.profesor', string="Profesor que imparte")
    alumnos = fields.Many2many('ciclos.alumno',string='Alumnos matriculados')
    ciclo = fields.Many2one('ciclos.cicloformativo', string='Ciclo')