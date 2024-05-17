from django.db import models
from django.contrib.auth.models import User
# for universal id 
import uuid 
import os
# pre_delete to delete the files associated to a row when row is deleted
from django.db.models.signals import pre_delete
from django.dispatch import receiver
#for automatic slug creation
from autoslug import AutoSlugField
from django.contrib.auth.models import Group
import boto3
from django.conf import settings


class Community(models.Model):
    def get_image_path(instance, filename):
        # Generate the filename using the id and extension from the original filename
        ext = filename.split('.')[-1]
        filename = f"{instance.name}.{ext}"
        # Return the final file path
        return f"communities_logos/{filename}"
    
    def save(self,*args, **kwargs):
        user = User.objects.filter(username=self.name).first()
        if not user:
            user = User.objects.create_user(username=self.name,password='pass')
            group = Group.objects.get(name='community')
            user.is_staff = True
            user.groups.add(group)
            user.save()
        super().save(*args, **kwargs)

    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=25)
    about = models.TextField(blank=True)
    description = models.TextField(blank=True,default=None,null=True)
    logo=models.ImageField(upload_to=get_image_path, default=None,blank=True)
    slug = AutoSlugField(populate_from='name',unique=True,default=None,null=True)

    def __str__(self):
        return self.name

class Clubs(models.Model):
    def save(self,*args, **kwargs):
        user = User.objects.filter(username=self.name).first()
        if not user:
            user = User.objects.create_user(username=self.name,password='pass')
            group = Group.objects.get(name='community')
            user.is_staff = True
            user.groups.add(group)
            user.save()
        super().save(*args, **kwargs)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=25)
    about = models.TextField(blank=True)
    description = models.TextField(blank=True,default=None,null=True)   
    slug = AutoSlugField(populate_from='name',unique=True,default=None,null=True) 

    def __str__(self):
        return self.name
    

class Fests(models.Model):
    def get_image_path(instance, filename):
        # Generate the filename using the id and extension from the original filename
        ext = filename.split('.')[-1]
        filename = f"{instance.name}.{ext}"
        # Return the final file path
        return f"fest_logos/{filename}"
    
    def save(self,*args, **kwargs):
        user = User.objects.filter(username=self.name).first()
        if not user:
            user = User.objects.create_user(username=self.name,password='pass')
            group = Group.objects.get(name='fest')
            user.is_staff = True
            user.groups.add(group)
            user.save()
        super().save(*args, **kwargs)
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=200 ,null=True)
    about = models.TextField(blank=True,default=None,null=True)
    description = models.TextField(blank=True,default=None,null=True)
    logo=models.ImageField(upload_to=get_image_path, default='default_image.jpg')
    slug = AutoSlugField(populate_from='name',unique=True,default=None,null=True)

    def __str__(self):
        return self.name
    

class Program(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(default=None,null=True)
    # conditions = HTMLField(blank=True,default=None,null=True)
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
        return f"news_images/{filename}"
       
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    body = models.TextField(default=None,null=True)
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
        return f"carousel_images/{filename}"
    
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
        return f"explore_images/{filename}"
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True,default=None,null=True)
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
        return f"explore_images/{filename}"
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to=get_image_path)
    #explore = models.ForeignKey(Explore,on_delete=models.CASCADE,default=uuid.uuid4,blank=True)

    
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
        image_path = str(instance.image)

        # Initialize AWS S3 client
        s3 = boto3.client('s3',
                          aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                          region_name=settings.AWS_S3_REGION_NAME)

        # Get bucket name and key from the image path
        bucket_name = settings.AWS_STORAGE_BUCKET_NAME
        
        # Delete the file from S3
        try:
            s3.delete_object(Bucket=bucket_name, Key=image_path)
        except Exception as e:
            print(f"An error occurred while deleting file from S3: {e}")


@receiver(pre_delete, sender=Fests)
@receiver(pre_delete, sender=Community)
def delete_image_file(sender, instance, **kwargs):
    # Check if the instance has an image file
    if instance.logo:
        # Get the path to the image file
        image_path = str(instance.logo)

        # Initialize AWS S3 client
        s3 = boto3.client('s3',
                          aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                          region_name=settings.AWS_S3_REGION_NAME)

        # Get bucket name and key from the image path
        bucket_name = settings.AWS_STORAGE_BUCKET_NAME
        
        # Delete the file from S3
        try:
            s3.delete_object(Bucket=bucket_name, Key=image_path)
        except Exception as e:
            print(f"An error occurred while deleting file from S3: {e}")


