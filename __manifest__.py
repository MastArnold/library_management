{
    'name': 'Library_Management',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_management_book_views.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'static/src/js/book_form.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}