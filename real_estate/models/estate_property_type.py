# -*- coding: utf-8 -*-
from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "real_estate.property.type"
    _description = "Property Type"

    name = fields.Char(required=True)
