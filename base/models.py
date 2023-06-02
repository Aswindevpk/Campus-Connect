from django.db import models
# from django.core.files.uploadedfile import InMemoryUploadedFile



class Carousel(models.Model):
    title = models.CharField( max_length=200)
    image = models.ImageField(upload_to='carousel_images/')
    
    def __str__(self):
        return self.title

class Program(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    time = models.TimeField(null=True)
    date = models.DateField(null=True)
    link = models.URLField()
    venue = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Bloodreq(models.Model):
    bloodGroup = models.CharField(max_length=3, choices=[
        ('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('O+','O+'),('O-','O-'),('AB+','AB+'),('AB-','AB-')
    ])
    contact = models.CharField(max_length=200)

    def __str__(self):
        return self.bloodGroup

class News(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=200)
    image = models.ImageField(upload_to='news_images',default='default_image.jpg')

    def __str__(self):
        return self.title

class Explore(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.CharField(max_length=200)
    image = models.ImageField(upload_to='explore_images')


    def __str__(self):
        return self.name
    
class Fests(models.Model):
    name=models.CharField(max_length=200 ,null=True)
    logo=models.ImageField(upload_to='fest_logos', default='default_image.jpg')

    def __str__(self):
        return self.name
    
class BloodDonation(models.Model):
    name = models.CharField(max_length=200)
    blood_type = models.ForeignKey(Bloodreq, on_delete=models.CASCADE)   
    roll_no = models.CharField(max_length=10) 
    phone = models.CharField(max_length=10)   

    def __str__(self):
        return self.name



