{
    'name': 'TO-DO',
    'version': '17.0.0.1.0',
    'author': 'Amr Gebil',
    'category': 'My_Addons',
    'description': """Module to tasks management""",
    'website': 'https://www.linkedin.com/in/amr-gebil-557a9024a/',
    'license': 'LGPL-3',
    'summary': 'task management',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/todo_view.xml'

    ],
    'assets': {
        'web.assets_backend': ['todo_management\static\src\property.css']

    },

    'application':True

}

