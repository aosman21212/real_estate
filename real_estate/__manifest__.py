# -*- coding: utf-8 -*-
# =============================================================================
#  Real Estate Ads
# -----------------------------------------------------------------------------
#  Location  : King Abdulaziz Branch Road, Riyadh, Saudi Arabia
#  Email     : sales@leapai.ai
#  Phone     : +966 53 553 3627
#  Website   : https://leapai.ai
#  Developer : Abdulkaraim Osman — Tech Manager | Backend Engineer | DevOps Engineer
#              at Bab International Corp For Specialized Services
#  LinkedIn  : https://www.linkedin.com/in/abdulkaraim-o-385b7a110/
# =============================================================================
{
    "name": "Real Estate Ads",
    "author": "abdi",
    "maintainer": "Abdulkaraim Osman",
    "support": "sales@leapai.ai",
    "version": "19.0.1.0.0",
    "description": "Real Estate module to show available properties",
    "category": "Sales",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_menus.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
