# -*- coding: utf-8 -*-
# Copyright 2020-now Al Hadi Tech - Pakistan
# License OPL-1

from odoo import SUPERUSER_ID, api
from . import models


def _uninstall_reset_changes(cr,registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['res.config.settings'].reset_values()
