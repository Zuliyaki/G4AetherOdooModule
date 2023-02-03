# -*- coding: utf-8 -*-
{
    'name': "Aether",

    'summary': """
        An app for managing psychologist and patients""",

    'description': """
        Allows:
            - Create new psychologist and patients
            - CRUD Daily Notes
            - Make appointments
    """,

    'author': "Aether",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/views.xml',
        'views/viewsDailyNotes.xml',
        'views/viewsMentalDisease.xml',
        'views/viewsAppointments.xml',
        'views/viewsDiagnosises.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}