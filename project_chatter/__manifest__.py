# -*- coding: utf-8 -*-
# Copyright 2020 Corail Technologie
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Project Chatter",
    "summary": "Add chatter on project form",
    "version": "12.0.1.0.0",
    "development_status": "Beta",
    "category": "Project",
    "website": "https://www.corail-technologie.com",
    "author": "Corail Technologie",
    "maintainers": ["foah"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "pre_init_hook": "",
    "post_init_hook": "",
    "post_load": "",
    "uninstall_hook": "",
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base",
        "project"
    ],
    "data": [
        "views/project_project_views.xml",
    ],
    "demo": [
    ],
    "qweb": [
    ]
}
