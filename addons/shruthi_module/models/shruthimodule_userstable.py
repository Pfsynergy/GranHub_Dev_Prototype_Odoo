from odoo import models, fields



class SHRUTHIModuleUsersTable(models.Model):
	_name = 'shruthimodule.userstable'	
	name = fields.Char('Title', required=True)	
	