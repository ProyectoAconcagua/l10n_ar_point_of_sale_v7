# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2008-2011 E-MIPS Electronica e Informatica <info@e-mips.com.ar>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from osv import osv, fields

class account_tax(osv.osv):
    _name = 'account.tax'
    _inherit = 'account.tax'
    _description = 'Tax'
    _columns = {
        'tax_group': fields.selection( [('vat','VAT'), ('perception','Perception'), ('retention','Retention'), ('internal','Internal Tax'), ('other','Other')], 'Tax Group', required=True,
            help="This is tax categorization."),
        'other_group': fields.char('Other Group', size=64),
        'is_exempt': fields.boolean('Exempt', help="Check this if this Tax represent Tax Exempts"),
        }

    _defaults = {
            'is_exempt': False,
            'tax_group': 'vat',
            }

account_tax()
