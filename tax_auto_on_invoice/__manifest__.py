# -*- coding: utf-8 -*-
# Copyright 2018 Ahmed Foudhaili <http://www.corail-technologie.com>
{
    'name': "Tax Auto on invoice",

    'summary': """
        Permet la declaration d'une taxe à ajouter automatiquement sur la facture (pas sur le produit)
        Exemple : Timbre Ficale""",

    'description': """
        Permet la declaration d'une tax à ajouter automatiquement sur la facture (pas sur le produit)
        Exemple : Timbre Ficale
    """,

    'author': 'Ahmed Foudhaili, '
              'Corail Technologie',
    'website': 'https://www.corail-technologie.com',
    'category': 'Accounting',
    'version': '12.0.1.0.0',
    'depends': ['base','account'],
    'data': [
       'views/views.xml',
    ],
   'installable': True,
    
}