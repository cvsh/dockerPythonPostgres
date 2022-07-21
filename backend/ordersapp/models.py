# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Orders(models.Model):
    id = models.TextField(db_column='Num', primary_key=True)  # Field name made lowercase.
    order_number = models.IntegerField(db_column='Order number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    price_usd = models.FloatField(db_column='Price_usd', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    price_rub = models.DecimalField(db_column='Price_rub', max_digits=13, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'

    def save(self, *args, **kwargs):
        self.price_rub = round(self.price_rub, 1)
        super(Orders, self).save(*args, **kwargs) 
