from django.db import models

class productCategory(models.Model):
    category = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True, editable=False)

    class Meta:
        app_label = 'product'
        db_table = 'product_category'

    def __str__(self):
        return self.category

class productList(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    desc = models.TextField(null=True, blank=True)
    images = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(productCategory, on_delete=models.CASCADE)

    class Meta:
        app_label = "product"
        db_table = "product_list"

    def __str__(self):
        return '(%s) %s -- %s'%(self.code, self.name, self.category)

