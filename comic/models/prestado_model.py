# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Prestado(models.Model):
    _name = 'biblioteca.prestado'
    _description = "Comics prestados"

    _rec_name = 'id'

    socio = fields.Many2one(
        'biblioteca.socio', 
        string="Socio",
    )
    comic = fields.Many2one(
        'biblioteca.comic',
        string='Comic',
    )
    inicio = fields.Date(string="Inicio", default=lambda self: fields.Date.today())
    fin = fields.Date("Fin")

    @api.constrains('inicio')
    def _check_start (self):
        for record in self:
            if record.inicio > fields.Date.today():
                raise ValidationError("La fecha de inicio no puede ser posterior al dia de hoy.")
            
    @api.constrains('fin')
    def _check_finish (self):
        for record in self:
            if record.fin < record.inicio:
                raise ValidationError("La fecha de fin no puede ser inferior al dia de inicio.")