# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (C) 2012 OpenERP - Team de Localización Argentina.
# https://launchpad.net/~openerp-l10n-ar-localization
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv

class product_category(osv.osv):
    _name = 'product.category'
    _inherit = 'product.category'

    _columns = {
        'base_amount': fields.float('Base Amount'),
	'percentage': fields.float('Percentage')
    }

    _default = {
	'base_amount': 0,
	'percentage': 0,
	}

product_category()

class product_product(osv.osv):
    _name = 'product.product'
    _inherit = 'product.product'


    def _fnct_display_base_amount(self, cr, uid, ids, field_name, args, context=None):
        res = {}
        if ids:
		res[ids[0]] = 0
		data = self.browse(cr,uid,ids,context=context)
		tmpl_id_data = self.pool.get('product.template').browse(cr,uid,data[0].product_tmpl_id.id,context=context)
		if tmpl_id_data.categ_id.id:
			categ_data = self.pool.get('product.category').read(cr,uid,tmpl_id_data.categ_id.id)
                        res[ids[0]] = categ_data['base_amount']
        else:
                res = None
        return res

    def _fnct_display_percentage(self, cr, uid, ids, field_name, args, context=None):
        res = {}
        if ids:
		res[ids[0]] = 0
		data = self.browse(cr,uid,ids,context=context)
		tmpl_id_data = self.pool.get('product.template').browse(cr,uid,data[0].product_tmpl_id.id,context=context)
		if tmpl_id_data.categ_id.id:
			categ_data = self.pool.get('product.category').read(cr,uid,tmpl_id_data.categ_id.id)
                        res[ids[0]] = categ_data['percentage']
        else:
                res = None
        return res


    _columns = {
        'base_amount': fields.function(_fnct_display_base_amount,string='Base Amount',type='float'),
        'percentage': fields.function(_fnct_display_percentage,string='Percentage',type='float'),
    }

product_product()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
