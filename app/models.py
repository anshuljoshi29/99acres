from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    area1 = models.CharField(max_length=255, null=True, blank=True)
    area2 = models.CharField(max_length=255, null=True, blank=True)
    locality = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    href = models.URLField()

    def __str__(self):
        return self.name
