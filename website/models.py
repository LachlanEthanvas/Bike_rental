from django.db import models

# Create your models here.
class Bike(models.Model):
    name=models.CharField(max_length=255)
    company=models.CharField(max_length=50)
    model=models.CharField(max_length=100)
    cost=models.IntegerField()
    colour=models.CharField(max_length=30)
    image= models.ImageField( upload_to='bike images')
    def __str__(self):
        return (str(self.name)+'. '+self.company+'-'+self.model+'-'+self.colour)

 
class Specfication(models.Model):
    BIKE_TYPE_CHOICES = (("CRUISER", "Cruiser"),("Touring", "Touring"),("Chopper", "Chopper"), ("Sports", "Sports"),)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, related_name='specifications')
    bike_type=models.CharField(choices=BIKE_TYPE_CHOICES,default="",max_length=50)
    displacement = models.PositiveSmallIntegerField(help_text="Displacement in cc")
    max_power = models.DecimalField(max_digits=5, decimal_places=2, help_text="Maximum power in bhp")
    max_torque = models.DecimalField(max_digits=5, decimal_places=2, help_text="Maximum torque in Nm")
    mileage_owner_reported = models.DecimalField(max_digits=5, decimal_places=2, help_text="Owner reported mileage in kmpl", null=True, blank=True)
    transmission_type = models.CharField(max_length=50, help_text="Type of transmission e.g., Chain Drive")
    transmission_gear_count = models.PositiveSmallIntegerField(help_text="Number of gears in the transmission", null=True, blank=True)

    def __str__(self):
        return f"Specifications for {self.bike}"