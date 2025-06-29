{
    'name': 'Library',
    'version': '17.0',
    'summary': 'Simple Library Management System',
    'author': 'Mostafa Amr ',
    'depends': ['base'],
    'data': [


         'views/library_book_view.xml',
          'views/library_loan_view.xml',


        'security/security_groups.xml',
         'security/recored_rules.xml',
        'security/ir.model.access.csv',
'reports/library_loan_templates.xml',
'reports/report_library_loan.xml',



    ],
    'installable': True,
    'application': True,
'license': 'LGPL-3',

}