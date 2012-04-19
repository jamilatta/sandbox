from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=60)
    def __unicode__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher)

    def __unicode__(self):
        return self.title
