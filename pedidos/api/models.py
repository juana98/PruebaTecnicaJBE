from django.db import models

class Driver(models.Model):

    id = models.IntegerField(primary_key=True,null = False)
    x = models.IntegerField(null = False)
    y = models.IntegerField(null = False)
    last_update = models.DateTimeField(verbose_name='last-update')

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['id']

class PickupLocation(models.Model):

    x_pickup = models.IntegerField()
    y_pickup = models.IntegerField()


class DestLocation(models.Model):

    x_dest = models.IntegerField()
    y_dest = models.IntegerField()
    

class Order(models.Model):

    date = models.DateTimeField()
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    pickup_location = models.OneToOneField(PickupLocation, on_delete=models.CASCADE, null=True)
    dest_location = models.OneToOneField(DestLocation, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.driver.id

