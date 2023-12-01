from django.db import models

# Create your models here.

class Amenities(models.Model):
    amenity = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.amenity

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_price = models.IntegerField()
    hotel_description = models.TextField()
    amenities = models.ManyToManyField(Amenities)
    banner_image = models.ImageField(upload_to="hotels")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.hotel_name

class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="hotels")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.hotel.hotel_name
