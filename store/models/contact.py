from django.db import models

class Query(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=500)
    subject = models.CharField(max_length=1000)
    message = models.TextField()

    def placeQuery(self):
        self.save()

    def __str__(self):
        return self.name