from django.db import models
# for universal id 
import uuid 

import os

# pre_delete to delete the files associated to a row when row is deleted
from django.db.models.signals import pre_delete
from django.dispatch import receiver

#for image manipulation to compress the image and change png - jpg
from PIL import Image
from io import BytesIO
from django.core.files import File



class Community(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=25)
    full_form = models.TextField(blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Fests(models.Model):
    def get_image_path(instance, filename):
        # Generate the filename using the id and extension from the original filename
        ext = filename.split('.')[-1]
        filename = f"{instance.id}.{ext}"
        # Return the final file path
        return f"media/fest_logos/{filename}"
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=200 ,null=True)
    full_form = models.TextField(blank=True)
    description = models.TextField()
    logo=models.ImageField(upload_to=get_image_path, default='default_image.jpg')


    # before saving the instance we’re reducing the image
    def save(self, *args, **kwargs):
        self.logo =self.convert_png_to_jpg(self.logo)
        new_image = self.reduce_image_size(self.logo)
        self.logo = new_image
        super().save(*args, **kwargs) 

    def convert_png_to_jpg(self, logo):
        if logo.name.lower().endswith('.png'):
            new_image = BytesIO()
            with Image.open(logo) as img:
                img = img.convert('RGB')
                img.save(new_image, 'JPEG')

            # Create a new image file with the converted JPEG data
            new_image.seek(0)
            return File(new_image, name=logo.name.replace('.png', '.jpg'))
        return logo 

    def reduce_image_size(self, image):
        img_size = image.size //1024
        img = Image.open(image)
        thumb_io = BytesIO()
        Quality = int((200 // img_size) * 70)
        img.save(thumb_io, 'jpeg', quality=Quality)
        image = File(thumb_io, name=image.name)
        return image

    def __str__(self):
        return self.name
    

class Program(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    time = models.TimeField(null=True)
    date = models.DateField(null=True)
    link = models.URLField(null=True,blank=True)
    venue = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200,blank=True)


    def __str__(self):
        return self.name



class News(models.Model):
    def get_image_path(instance, filename):
        # Generate the filename using the id and extension from the original filename
        ext = filename.split('.')[-1]
        filename = f"{instance.id}.{ext}"
        # Return the final file path
        return f"media/news_images/{filename}"
       
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to=get_image_path,default='default_image.jpg')
    created_by = models.CharField(max_length=200,blank=True)

     # before saving the instance we’re reducing the image
    def save(self, *args, **kwargs):
        self.image =self.convert_png_to_jpg(self.image)
        new_image = self.reduce_image_size(self.image)
        self.image = new_image
        super().save(*args, **kwargs) 

    def convert_png_to_jpg(self, image):
        if image.name.lower().endswith('.png'):
            new_image = BytesIO()
            with Image.open(image) as img:
                img = img.convert('RGB')
                img.save(new_image, 'JPEG')

            # Create a new image file with the converted JPEG data
            new_image.seek(0)
            return File(new_image, name=image.name.replace('.png', '.jpg'))
        return image 

    def reduce_image_size(self, image):
        img_size = image.size //1024
        img = Image.open(image)
        thumb_io = BytesIO()
        Quality = int((200 // img_size) * 70)
        img.save(thumb_io, 'jpeg', quality=Quality)
        image = File(thumb_io, name=image.name)
        return image

    def __str__(self):
        return self.title
    

class Carousel(models.Model):
    def get_image_path(instance, filename):
        # Generate the filename using the id and extension from the original filename
        ext = filename.split('.')[-1]
        filename = f"{instance.id}.{ext}"
        # Return the final file path
        return f"media/carousel_images/{filename}"
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField( max_length=200)
    image = models.ImageField(upload_to=get_image_path)
    program = models.ForeignKey(Program, on_delete=models.CASCADE,default=uuid.uuid4,null=True,blank=True)
    news = models.ForeignKey(News,on_delete=models.CASCADE,default=uuid.uuid4,null=True,blank=True)
    created_by = models.CharField(max_length=200,blank=True)


    # before saving the instance we’re reducing the image
    def save(self, *args, **kwargs):
        self.image =self.convert_png_to_jpg(self.image)
        new_image = self.reduce_image_size(self.image)
        self.image = new_image
        super().save(*args, **kwargs) 

    def convert_png_to_jpg(self, image):
        if image.name.lower().endswith('.png'):
            new_image = BytesIO()
            with Image.open(image) as img:
                img = img.convert('RGB')
                img.save(new_image, 'JPEG')

            # Create a new image file with the converted JPEG data
            new_image.seek(0)
            return File(new_image, name=image.name.replace('.png', '.jpg'))
        return image 

    def reduce_image_size(self, image):
        img_size = image.size //1024
        img = Image.open(image)
        thumb_io = BytesIO()
        Quality = int((200 // img_size) * 70)
        img.save(thumb_io, 'jpeg', quality=Quality)
        image = File(thumb_io, name=image.name)
        return image

    def __str__(self):
        return self.title



class Explore(models.Model):
    def get_image_path(instance, filename):
        # Generate the filename using the id and extension from the original filename
        ext = filename.split('.')[-1]
        filename = f"{instance.id}.{ext}"
        # Return the final file path
        return f"media/explore_images/{filename}"
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.CharField(max_length=200)
    image = models.ImageField(upload_to=get_image_path)

     # before saving the instance we’re reducing the image
    def save(self, *args, **kwargs):
        self.image =self.convert_png_to_jpg(self.image)
        new_image = self.reduce_image_size(self.image)
        self.image = new_image
        super().save(*args, **kwargs) 

    def convert_png_to_jpg(self, image):
        if image.name.lower().endswith('.png'):
            new_image = BytesIO()
            with Image.open(image) as img:
                img = img.convert('RGB')
                img.save(new_image, 'JPEG')

            # Create a new image file with the converted JPEG data
            new_image.seek(0)
            return File(new_image, name=image.name.replace('.png', '.jpg'))
        return image 

    def reduce_image_size(self, image):
        img_size = image.size //1024
        img = Image.open(image)
        thumb_io = BytesIO()
        Quality = int((200 // img_size) * 70)
        img.save(thumb_io, 'jpeg', quality=Quality)
        image = File(thumb_io, name=image.name)
        return image

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
    name = models.CharField(max_length=25)

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
def delete_image_file(sender, instance, **kwargs):
    # Check if the instance has an image file
    if instance.logo:
        # Get the path to the image file
        image_path = instance.logo.path
        # Check if the file exists and delete it
        if os.path.exists(image_path):
            os.remove(image_path)