from django.db import models
from django.utils.text import slugify

# Create your models here.
class JobPost(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(max_length=5000)
  post_date = models.DateTimeField(auto_now_add=True)
  salary = models.IntegerField()
  company = models.CharField(max_length=200)
  company_location = models.CharField(max_length=500)
  slug = models.SlugField(null=True, max_length=40, unique=True)
  
  def __str__(self):
    return f"{self.company} - {self.title}"
  
  def save(self, *args, **kwargs):
    if not self.id:
      self.slug = slugify(self.title)
    return super(JobPost, self).save(*args,**kwargs)