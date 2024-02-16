from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    no_ktp = fields.Char()
    tanggal_lahir = fields.Date()