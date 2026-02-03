# -*- coding: utf-8 -*-

{
    'name': "Location de véhicules",

    'summary': """
        Outil de gestion de location de véhicules""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Antoine Moulin",
    'website': "https://c2i-revision.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory/cars',
    'version': '18.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'mail', 'utm', 'website', 'portal', 'contacts', 'crm'],

    'application': True,
    'license': 'AGPL-3',
    # always loaded
    'data': [
        'security/rentcars_security.xml',
        'security/ir.model.access.csv',
        'views/rentcars_menu.xml',
        'views/vehicle_views.xml',
        'views/garage_views.xml',
        'views/garage_kanban_view.xml',
        'views/booking_views.xml',
        "views/reparation_kanban_view.xml",
        'views/vehicle_list_template.xml',
        'views/vehicle_detail_template.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/rentcars.vehicle.csv',
        'demo/rentcars.garage.csv',
        'demo/demo.xml'
    ],
}
