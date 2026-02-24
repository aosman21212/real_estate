# -*- coding: utf-8 -*-
"""Fix database records that still reference the old model name estate.property."""


def post_init_hook(env):
    # Odoo 19 passes env; older versions pass (cr, registry) - support both
    if hasattr(env, "cr"):
        pass  # env is an Environment
    else:
        from odoo import api, SUPERUSER_ID
        env = api.Environment(env, SUPERUSER_ID, {})  # env was cr
    env["ir.actions.act_window"].search([
        ("res_model", "=", "estate.property"),
    ]).write({"res_model": "real_estate.property"})
