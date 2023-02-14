# -*- coding: utf-8 -*-
{
    'name': "Hospital",  # Titulo del módulo
    'summary': "Gestionar medicos y pacientes",  # Resumen de la funcionaliadad
    'description': """
Gestor de hospital
==============
    """,  

    'application': True,
    'author': "DAMB",
    'website': "http://iesjoanramis.org",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/medicos.xml',
        'views/pacientes.xml',
        'views/diagnosticos.xml'
    ],
}
