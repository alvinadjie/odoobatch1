# -*- coding: utf-8 -*-
{
    'name': "movie app",

    'summary': """
        Movie app""",

    'description': """
        Database movie
    """,

    'author': "Alvin Adji",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'digest'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
    ],
}