# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Movie(models.Model):
	_name = 'movie'
	_description = 'Movie'
	_inherit = ['mail.thread']

	name = fields.Char(string='Judul', required=1, tracking=1)
	date_release = fields.Date()
	artist_ids = fields.Many2many('artist')
	studio_id = fields.Many2one('studio')
	rating = fields.Float(tracking=1)
	review_ids = fields.One2many('review', 'movie_id')


class Artist(models.Model):
	_name = 'artist'
	_description = 'Artist'

	name = fields.Char(required=1)
	date_birth = fields.Date()

class Studio(models.Model):
	_name = 'studio'
	_description = 'Studio'

	name = fields.Char(required=1)

class Review(models.Model):
	_name = 'review'
	_description = 'Review'

	movie_id = fields.Many2one('movie')
	review = fields.Text(required=1)


	

	