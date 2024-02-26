# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class SaleOrder(models.Model):
	_inherit = 'sale.order'

	kode = fields.Char()

	a = fields.Integer()
	b = fields.Integer()
	c = fields.Integer()
	d = fields.Integer(compute='hitung_d')
	nilai = fields.Char(compute='konversi_nilai')

	def hitung_c(self):
		self.c = self.a + self.b

	@api.depends('a','b','c')
	def hitung_d(self):
		for rec in self:
			rec.d = rec.a + rec.b + rec.c

	@api.depends('d')
	def konversi_nilai(self):
		for rec in self:
			if rec.d > 85:
				rec.nilai = 'A'
			else:
				rec.nilai = 'B'

	@api.onchange('a','b')
	def onchange_hitung_c(self):
		self.c = self.a + self.b

	def action_cancel(self):
		if self.nilai == 'A':
			raise ValidationError('Tidak bisa cancel')
		res = super(SaleOrder,self).action_cancel()
		return res

	@api.model
	def create(self,vals):
		print(vals)
		if 'a' in vals and vals['a'] < 10:
			raise ValidationError('Nilai A minimal 10')
		res = super(SaleOrder,self).create(vals)
		return res

	def write(self,vals):
		print(vals)
		if 'a' in vals and vals['a'] < 10:
			raise ValidationError('Nilai A minimal 10')
		res = super(SaleOrder,self).write(vals)
		return res

	def unlink(self):
		if self.state != 'draft':
			raise ValidationError('Tidak Boleh dihapus')
		res = super(SaleOrder,self).unlink()
		return res
