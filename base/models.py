from django.db import models
# for universal id 
import uuid 

import os

# pre_delete to delete the files associated to a row when row is deleted
from django.db.models.signals import pre_delete
from django.dispatch import receiver

#for automatic slug creation
from autoslug import AutoSlugField







class Community(models.Model):
    def get_image_path(instance, filename):
        # Generate the filename using the id and extension from the original filename
        ext = filename.split('.')[-1]
        filename = f"{instance.name}.{ext}"
        # Return the final file path
        return f"media/communities_logos/{filename}"
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=25)
    about = models.TextField(blank=True)
    description = models.TextField()
    logo=models.ImageField(upload_to=get_image_path, default=None,blank=True)
    slug = AutoSlugField(populate_from='name',unique=True,default=None,null=True)

    def __str__(self):
        return self.name

class Clubs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=25)
    about = models.TextField(blank=True)
    description = models.TextField()   
    slug = AutoSlugField(populate_from='name',unique=True,default=None,null=True) 

    def __str__(self):
        return self.name
    

class Fests(models.Model):
    def get_image_path(instance, filename):
        # Generate the filename using the id and extension from the original filename
        ext = filename.split('.')[-1]
        filename = f"{instance.name}.{ext}"
        # Return the final file path
        return f"media/fest_logos/{filename}"
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=200 ,null=True)
    about = models.TextField(blank=True)
    description = models.TextField()
    logo=models.ImageField(upload_to=get_image_path, default='default_image.jpg')
    slug = AutoSlugField(populate_from='name',unique=True,default=None,null=True)

    def __str__(self):
        return self.name
    

class Program(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    time = models.TimeField(null=True)
    date = models.DateField(null=True)
    link = models.URLField(null=True,blank=True)
    venue = models.CharField(max_length=200,null=True,blank=True)
    created_by = models.CharField(max_length=200,blank=True)
    slug = AutoSlugField(populate_from='name',unique=True,default=None,null=True)

    def __str__(self):
        return self.name


class News(models.Model):
    def get_image_path(instance, filename):
        # Generate the filename using the id and extension from the original filename
        ext = filename.split('.')[-1]
        filename = f"{instance.title}.{ext}"
        # Return the final file path
        return f"media/news_images/{filename}"
       
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=get_image_path)
    created_by = models.CharField(max_length=200,blank=True)
    slug = AutoSlugField(populate_from='title',unique=True,default=None,null=True)

    def __str__(self):
        return self.title
    


class Carousel(models.Model):
    def get_image_path(instance, filename):
        # Generate the filename using the id and extension from the original filename
        ext = filename.split('.')[-1]
        filename = f"{instance.title}.{ext}"
        # Return the final file path
        return f"media/carousel_images/{filename}"
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField( max_length=200)
    image = models.ImageField(upload_to=get_image_path)
    program = models.ForeignKey(Program, on_delete=models.CASCADE,default=uuid.uuid4,null=True,blank=True)
    news = models.ForeignKey(News,on_delete=models.CASCADE,default=uuid.uuid4,null=True,blank=True)
    created_by = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.title



class Explore(models.Model):
    def get_image_path(instance, filename):
        # Generate the filename using the id and extension from the original filename
        ext = filename.split('.')[-1]
        filename = f"{instance.name}.{ext}"
        # Return the final file path
        return f"media/explore_images/{filename}"
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.CharField(max_length=200)
    image = models.ImageField(upload_to=get_image_path)
    slug = AutoSlugField(populate_from='name',unique=True,default=None,null=True)

    def __str__(self):
        return self.name
    
class Exploreimg(models.Model):
    def get_image_path(instance, filename):
        # Generate the filename using the id and extension from the original filename
        ext = filename.split('.')[-1]
        filename = f"{instance.id}.{ext}"
        # Return the final file path
        return f"media/explore_images/{filename}"
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to=get_image_path)
    explore = models.ForeignKey(Explore,on_delete=models.CASCADE,default=uuid.uuid4,blank=True)

    
class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Bloodreq(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bloodGroup = models.CharField(max_length=3, choices=[
        ('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('O+','O+'),('O-','O-'),('AB+','AB+'),('AB-','AB-')
    ])

    def __str__(self):
        return self.bloodGroup   

class BloodDonation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    blood_type = models.ForeignKey(Bloodreq, on_delete=models.CASCADE)   
    roll_no = models.CharField(max_length=8,unique=True) 
    phone = models.CharField(max_length=10, unique=True) 
    course =  models.ForeignKey(Course, on_delete=models.SET_NULL,blank=True,null=True) 

    def __str__(self):
        return self.name

class BloodDonatedStudents(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    blood_type = models.CharField(max_length=3)   
    roll_no = models.CharField(max_length=8,unique=True) 
    phone = models.CharField(max_length=10, unique=True)  
    donated_on = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

    






# deletes the image file in the directory when the row associated to it deleted
@receiver(pre_delete, sender=Carousel)
@receiver(pre_delete, sender=Explore)
@receiver(pre_delete, sender=News)
@receiver(pre_delete, sender=Exploreimg)
def delete_image_file(sender, instance, **kwargs):
    # Check if the instance has an image file
    if instance.image:
        # Get the path to the image file
        image_path = instance.image.path
        print(image_path)
        # Check if the file exists and delete it
        if os.path.exists(image_path):
            os.remove(image_path)


@receiver(pre_delete, sender=Fests)
@receiver(pre_delete, sender=Community)
def delete_image_file(sender, instance, **kwargs):
    # Check if the instance has an image file
    if instance.logo:
        # Get the path to the image file
        image_path = instance.logo.path
        # Check if the file exists and delete it
        if os.path.exists(image_path):
            os.remove(image_path)