# -*- coding: utf-8 -*-
from odoo import fields, models


class EstatePropertyTag(models.Model):
    _name = "real_estate.property.tag"
    _description = "Property Tag"

    name = fields.Char(required=True)
    color = fields.Integer("Color Index")
