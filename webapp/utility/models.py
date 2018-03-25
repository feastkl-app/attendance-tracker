from django.db import models

# Create your models here.

class AbstractBaseDate(models.Model):
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class AbstractBaseType(AbstractBaseDate):
    name = models.CharField(max_length=32, blank=False)
    remarks = models.CharField(max_length=64, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
