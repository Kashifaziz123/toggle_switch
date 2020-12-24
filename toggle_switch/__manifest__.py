# -*- coding: utf-8 -*-
# Copyright 2020-now Al Hadi Tech - Pakistan
# License OPL-1
{
    'name':'Toggle Switch',
    'license': 'OPL-1',
    'category':'Extra Tools',
    'version': '1.0.1',
    'description':"Defaults Boolean Fields into Toggle Switch & also Change its Shapes and Color Properties",
    'author': 'Kashif Aziz',
    'price':30,'currency': 'EUR',
    'website': 'https://alhaditech.com',
    'depends': ['base','base_setup','web'],
    'images': ['static/description/icon.png'],
    'data': [
            "views/assets.xml",
            "views/toggle_switch.xml"
        ],
    'installable': True,
    'auto_install': False,
    "uninstall_hook": "_uninstall_reset_changes",
}
