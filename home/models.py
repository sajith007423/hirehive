from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class profile(models.Model):
    ACCOUNT_TYPE_CHOICES = (
        ("company", "company account"),
        ("candidate", "candidate account"),
        )
    user = models.CharField(max_length=100,primary_key=True)
    account_type = models.CharField(max_length=10,default='', choices=ACCOUNT_TYPE_CHOICES)
    phone_number = models.CharField(max_length=12,blank=True,default='')
    birth_date = models.DateField(null=True,blank=True,default='')
    profile_picture = models.ImageField(upload_to='profilephoto')
    bio = models.TextField(max_length=500,default='')
    instagram_username=models.CharField(max_length=100,default='')
    linkedin_link=models.CharField(max_length=400,default='')
    twitter_username=models.CharField(max_length=100,default='')
    whatsapp_number = models.CharField(max_length=10,default='')
    address=models.CharField(max_length=400,default='')
    skills=models.TextField(max_length=400,default='')
    qualifications=models.TextField(max_length=400,default='')
    achievement=models.TextField(max_length=400,default='')
    
class jobOffer(models.Model):
    user = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=500,default='')
    job_salary = models.CharField(max_length=100,default='')
    phone_number = models.CharField(max_length=12,blank=True,default='')
    posting_photo = models.ImageField(upload_to='jobposts')
    link = models.CharField(max_length=2500,blank=True,default='')
    
class courseOffer(models.Model):
    user = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=500,default='')
    course_fee = models.CharField(max_length=100,default='')
    phone_number = models.CharField(max_length=12,blank=True,default='')
    posting_photo = models.ImageField(upload_to='courseposts')
    link = models.CharField(max_length=2500,blank=True,default='')
    
class interviewOffer(models.Model):
    user = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=500,default='')
    phone_number = models.CharField(max_length=12,blank=True,default='')
    posting_photo = models.ImageField(upload_to='interviewposts')
    link = models.CharField(max_length=2500,blank=True,default='')
    
    
    
    