# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import api, fields, models


class EstatePropertyOffer(models.Model):
    _name = "real_estate.property.offer"
    _description = "Property Offer"
    _order = "price desc"

    price = fields.Float("Price", required=True)
    validity = fields.Integer("Validity (days)", default=7)
    deadline = fields.Date(
        "Deadline",
        compute="_compute_deadline",
        store=True,
        inverse="_inverse_deadline",
    )
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    property_id = fields.Many2one(
        "real_estate.property",
        string="Property",
        required=True,
        ondelete="cascade",
    )
    status = fields.Selection(
        [
            ("accepted", "Accepted"),
            ("refused", "Refused"),
        ],
        copy=False,
    )

    @api.depends("create_date", "validity")
    def _compute_deadline(self):
        for record in self:
            if record.create_date:
                record.deadline = record.create_date.date() + timedelta(
                    days=record.validity
                )
            else:
                record.deadline = fields.Date.today() + timedelta(
                    days=record.validity
                )

    @api.model_create_multi
    def create(self, vals_list):
        offers = super().create(vals_list)
        for offer in offers:
            if offer.property_id.state == "new":
                offer.property_id.state = "offer_received"
        return offers

    def _inverse_deadline(self):
        for record in self:
            if record.deadline and record.create_date:
                record.validity = (
                    record.deadline - record.create_date.date()
                ).days

    def action_accept(self):
        self.ensure_one()
        self.write({"status": "accepted"})
        return self.property_id.write({
            "state": "offer_accepted",
            "selling_price": self.price,
        })

    def action_refuse(self):
        self.ensure_one()
        return self.write({"status": "refused"})
