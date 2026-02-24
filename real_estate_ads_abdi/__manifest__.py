{
    "name": "Real Estate Ads",
    "author": "abيdi",
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
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
