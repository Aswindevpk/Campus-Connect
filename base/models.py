from django.db import models
import uuid

import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver





class Carousel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField( max_length=200)
    image = models.ImageField(upload_to='carousel_images/')

    def __str__(self):
        return self.title

class Program(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    time = models.TimeField(null=True)
    date = models.DateField(null=True)
    link = models.URLField()
    venue = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Bloodreq(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bloodGroup = models.CharField(max_length=3, choices=[
        ('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('O+','O+'),('O-','O-'),('AB+','AB+'),('AB-','AB-')
    ])

    def __str__(self):
        return self.bloodGroup

class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=200)
    image = models.ImageField(upload_to='news_images',default='default_image.jpg')

    def __str__(self):
        return self.title

class Explore(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.CharField(max_length=200)
    image = models.ImageField(upload_to='explore_images')


    def __str__(self):
        return self.name
    
class Fests(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=200 ,null=True)
    logo=models.ImageField(upload_to='fest_logos', default='default_image.jpg')

    def __str__(self):
        return self.name
    
class BloodDonation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    blood_type = models.ForeignKey(Bloodreq, on_delete=models.CASCADE)   
    roll_no = models.CharField(max_length=8,unique=True) 
    phone = models.CharField(max_length=10, unique=True)   

    def __str__(self):
        return self.name



class BloodDonatedStudents(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    blood_type = models.CharField(max_length=3)   
    roll_no = models.CharField(max_length=8,unique=True) 
    phone = models.CharField(max_length=10, unique=True)   

    def __str__(self):
        return self.name
    




# deletes the image file in the directory when the row associated to it deleted
@receiver(pre_delete, sender=[Carousel, Explore, News])
def delete_image_file(sender, instance, **kwargs):
    # Check if the instance has an image file
    if instance.image:
        # Get the path to the image file
        image_path = instance.image.path
        # Check if the file exists and delete it
        if os.path.exists(image_path):
            os.remove(image_path)

@receiver(pre_delete, sender=Fests)
def delete_image_file(sender, instance, **kwargs):
    # Check if the instance has an image file
    if instance.logo:
        # Get the path to the image file
        image_path = instance.logo.path
        # Check if the file exists and delete it
        if os.path.exists(image_path):
            os.remove(image_path)