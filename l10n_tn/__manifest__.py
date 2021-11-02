# © 2019 Ahmed Foudhaili <ahmed.foudhaili@corail-technologie.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Tunisian Accounting',
    'desc' : 'Tunisian accounting chart and tax localization',
    'version': '12.0.1.0.0',
    'license': '',
    'category': 'Localization',
    'author': 'Ahmed Foudhaili, '
              'Corail Technologie',
    'website': 'https://www.corail-technologie.com',
    'depends': [
        'account'
    ],
    'data': [
        'data/account_chart_template_data.xml',
        'data/account_chart_template_configure_data.xml',
        'data/account.account.template.csv',
        'data/account_tax_data.xml',
    ],
    'installable': True,
}
