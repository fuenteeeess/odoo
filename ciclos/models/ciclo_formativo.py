from odoo import models, fields

class CicloFormativo(models.Model):
    _name = 'ciclos.cicloformativo'
    _description = 'Ciclo formativo'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)
    modulos = fields.One2many('ciclos.modulo', 'ciclo', string='Modulos que incluye')