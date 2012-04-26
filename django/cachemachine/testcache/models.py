from django.db import models
import caching.base 
# Create your models here.

class Example(caching.base.CachingMixin, models.Model):
    objects = caching.base.CachingManager()
    filed0 = models.CharField(max_length=64) 

    def __unicode__(self):
      return self.filed0

