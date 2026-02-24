# -*- coding: utf-8 -*-
from odoo import api, fields, models


class EstateProperty(models.Model):
    _name = "real_estate.property"
    _description = "Real Estate Property"

    name = fields.Char("Title", required=True)
    property_type_id = fields.Many2one(
        "real_estate.property.type",
        string="Property Type",
        ondelete="restrict",
    )
    postcode = fields.Char("Postcode")
    date_availability = fields.Date(
        "Available From",
        default=lambda self: fields.Date.add(fields.Date.today(), months=3),
    )
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", readonly=True)
    bedrooms = fields.Integer("Bedrooms", default=2)
    living_area = fields.Integer("Living Area (sqm)")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage", default=False)
    garden = fields.Boolean("Garden", default=False)
    garden_area = fields.Integer("Garden Area (sqm)")
    total_area = fields.Integer(
        "Total Area (sqm)", compute="_compute_total_area", store=True
    )
    description = fields.Text("Description")
    tag_ids = fields.Many2many(
        "real_estate.property.tag",
        string="Tags",
    )
    offer_ids = fields.One2many(
        "real_estate.property.offer",
        "property_id",
        string="Offers",
    )
    offer_count = fields.Integer(compute="_compute_offer_count", string="Offer Count")
    best_price = fields.Float(
        compute="_compute_best_price", string="Best Offer", store=True
    )
    state = fields.Selection(
        [
            ("new", "NEW"),
            ("offer_received", "OFFER RECEIVED"),
            ("offer_accepted", "OFFER ACCEPTED"),
            ("sold", "SOLD"),
            ("canceled", "Canceled"),
        ],
        string="Status",
        default="new",
        required=True,
    )

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + (record.garden_area or 0)

    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped("price") or [0])

    def action_sold(self):
        return self.write({"state": "sold"})

    def action_cancel(self):
        return self.write({"state": "canceled"})
