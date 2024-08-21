from odoo import models, fields, api


class Property(models.Model):
    _name = 'todo.task'
    _description = "Task"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Task Name", required=True, size=10, tracking=1)
    partner_id = fields.Many2one('res.partner',required=True, string='Assign To', tracking=1)
    description = fields.Text(string="Description",required=True, tracking=1)
    date = fields.Date(string="Due Date", required=True, tracking=1)
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], default='new', tracking=1)

    def action_new(self):
        for rec in self:
            rec.state = 'new'


    def action_in_progress(self):
        for rec in self:
            rec.state = 'in_progress'

    def action_completed(self):
        for rec in self:
            rec.state = 'completed'

