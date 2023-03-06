# -*- coding: utf-8 -*-
{
    'name': "Ciclos",  # Titulo del módulo
    'summary': "Gestión de ciclos formativos",  # Resumen de la funcionaliadad
    'description': "Gestor de ciclos formativos",  

    'application': True,
    'author': "Alejandro Fuentes",
    'website': "http://iesjoanramis.org",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/ciclos_formativos.xml',
        'views/modulos.xml',
        'views/alumnos.xml',
        'views/profesores.xml'
    ],
}
