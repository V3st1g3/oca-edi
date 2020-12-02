# Copyright 2015-2016 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, models


class AccountInvoice(models.Model):
    _inherit = "account.move"

    def name_get(self):
        """Add amount_untaxed in name_get of invoices"""
        res = super().name_get()
        if self.env.context.get("invoice_show_amount"):
            new_res = []
            for (inv_id, name) in res:
                inv = self.browse(inv_id)
                # I didn't find a python method to easily display
                # a float + currency symbol (before or after)
                # depending on lang of context and currency
                name += _(" Amount w/o tax: %s %s") % (
                    inv.amount_untaxed,
                    inv.currency_id.name,
                )
                new_res.append((inv_id, name))
            return new_res
        return res
