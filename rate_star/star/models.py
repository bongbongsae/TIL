from django.db import models

# Create your models here.
class Star(models.Model) :
    id = models.IntegerField(primary_key=True)
    star_rate = models.IntegerField(db_column='rate', blank=True, null=True)

class StarRate(models.Model):
    id = models.IntegerField(primary_key=True)
    rate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'star_rate'
