from django.db import models

class Coupon(models.Model):
    name = models.CharField(max_length=500)
    off = models.IntegerField()
    total_required = models.IntegerField()

    def __str__(self):
        return self.name


    @staticmethod
    def get_coupon(name):
        try:
            return Coupon.objects.get(name=name)
        except:
            return False