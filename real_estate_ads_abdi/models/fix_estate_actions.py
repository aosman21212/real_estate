# -*- coding: utf-8 -*-
"""One-time fix for actions that still reference estate.property."""

from odoo import models


class FixEstateActions(models.TransientModel):
    _name = "real_estate.fix.actions"
    _description = "Fix estate.property references"

    def fix_actions(self):
        """Update any window actions still pointing to estate.property."""
        self.env["ir.actions.act_window"].search([
            ("res_model", "=", "estate.property"),
        ]).write({"res_model": "real_estate.property"})
        return True
