# -*- coding: utf-8 -*-
{
    'name': "lubon_suppliers",

    'summary': """
        Tools to import supplier priceslists into products. 
        """,

    'description': """
        Supports getting files with ftp, manual upload or reading from unix file system.
    """,

    'author': "Lubon bvba",
    'website': "http://www.lubon.be",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '8.0.0.9.0',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','sale', 'stock','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'security/ir.model.access.csv',
        'views/lubon_suppliers.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}