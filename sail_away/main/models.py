from django.db import models

# Create your models here.


class Crew(models.Model):
    crew_id = models.AutoField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    bio = models.TextField()
    picture = models.ImageField(upload_to='crew/')


class Boat(models.Model):
    boat_id = models.AutoField()
    name = models.CharField(max_length=30)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    length = models.FloatField()
    max_people = models.IntegerField()


class Booking(models.Model):
    booking_id = models.BigAutoField()
    head_count = models.IntegerField(blank=False)
    start = models.DateTimeField(blank=False)
    end = models.DateTimeField(blank=False)


class Guest(models.Model):
    guest_id = models.BigAutoField()
    head = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    dob = models.DateField(blank=False)
    address = models.ForeignKey(
        'Address', on_delete=models.PROTECT, blank=False)
    emergency_contact = models.ForeignKey('Contact', on_delete=models.PROTECT)
    booking = models.ForeignKey('Booking', on_delete=models.CASCADE)


class Address(models.Model):
    address_id = models.BigAutoField()
    street = models.CharField(max_length=100, blank=False)
    apt = models.IntegerField()
    city = models.CharField(max_length=50, blank=False)
    zip_code = models.IntegerField(blank=False)
    country = models.CharField(max_lenght=50, blank=False)


class Contact(models.Model):
    contact_id = models.BigAutoField()
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    phone = models.BigIntegerField()
