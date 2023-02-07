# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Socio(models.Model):
    _name = 'biblioteca.socio'
    _description = "Socios de la biblioteca"

    nombre = fields.Char("Nombre", required=True)
    apellidos = fields.Char("Apellidos")
    identificador = fields.Char("Identificador", required=True)