from sre_parse import State
from types import CoroutineType
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Skill(models.Model):
  name = models.CharField(max_length=200)
  
  def __str__(self):
    return self.name
  
class Author(models.Model):
  name = models.CharField(max_length=200)
  company  = models.CharField(max_length=200)
  designation = models.CharField(max_length=200)
  def __str__(self):
    return f"{self.company} - {self.name} - {self.designation}"
    
class Location(models.Model):
  street = models.CharField(max_length=200)
  city = models.CharField(max_length=200)
  state = models.CharField(max_length=200)
  country = models.CharField(max_length=200)
  
  def __str__(self):
    return f"{self.state} - {self.street}"

class JobPost(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(max_length=5000)
  post_date = models.DateTimeField(auto_now_add=True)
  salary = models.IntegerField()
  company = models.CharField(max_length=200)
  company_location = models.CharField(max_length=500)
  location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)
  expiry = models.DateField(null=True)
  slug = models.SlugField(null=True, max_length=40, unique=True)
  author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
  skills = models.ManyToManyField(Skill)
  
  def __str__(self):
    return f"{self.company} - {self.title}"
  
  def save(self, *args, **kwargs):
    if not self.id:
      self.slug = slugify(self.title)
    return super(JobPost, self).save(*args,**kwargs)