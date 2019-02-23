from django.db import models

# Create your models here.
class Info(models.Model):

    crop = models.CharField(max_length=255, null=False)

    season = models.CharField(max_length=255, null=False)

    grow_time = models.CharField(max_length=255, null=False)

    to = models.CharField(max_length=255, null=False)

    period = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.crop, self.season, self.grow_time, self.period)