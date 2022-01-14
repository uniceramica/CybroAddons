from odoo import models,fields,api
import re

class ProductBrand(models.Model):
    _inherit = 'product.template'

    brand_id = fields.Many2one('product.brand',string='Brand')

class BrandProduct(models.Model):
    _name = 'product.brand'


    name= fields.Char(String="Name")
    brand_image = fields.Binary()
    member_ids = fields.One2many('product.template','brand_id')
    product_count = fields.Char(String='Product Count',compute='get_count_products',store=True)

    @api.depends('member_ids')
    def get_count_products(self):
        self.product_count = len(self.member_ids)

class BrandPivot(models.Model):
    _inherit = 'sale.report'

    brand_id=fields.Many2one ('product.brand' ,string='Brand')

    def _query(self):
        res = super(BrandPivot, self)._query()
        res = re.sub(re.escape("t.categ_id as categ_id,"), "t.categ_id as categ_id,\n\tt.brand_id as brand_id,", res, flags=re.IGNORECASE)
        res = res.replace("t.categ_id,","t.categ_id,\n\tt.brand_id,",2)
        return res

