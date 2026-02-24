{
    "name": "Real Estate Ads",
    "author": "abdukarim osman , based on the module real_estate_ads",
    "version": "19.0.1.1.0",
    "description": "Real Estate module to show available properties",
    "category": "Sales",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_menus.xml",
        "data/fix_estate_actions_data.xml",
    ],
    "post_init_hook": "post_init_hook",
    "images": ["static/description/cover.png"],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
