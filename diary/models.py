from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Neighborhood(models.Model):
  category=models.CharField(max_length=50)
  diary_image=models.ImageField(upload_to='hood/',default='city.jpeg')
  entries=models.IntegerField()

  def __str__(self):
    return self.name
  def save_hood(self):
    self.save()
  def delete_hood(self):
    self.delete()

  @classmethod
  def view_neigborhood(cls,neighborhood_id):
    hood=cls.objects.filter(id=neighborhood_id)
    return hood

class NeighborProfile(models.Model):
  name=models.CharField(max_length=60)
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  neighborhood=models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
  email=models.CharField(max_length=100)
  prof_pic=models.ImageField(upload_to='profiles/',default='avatar.png')

  def __str__(self):
    return self.name
  def save_neighbour(self):
    self.save()
  def delete_neighbour(self):
    self.delete()

class Business(models.Model):
  name=models.CharField(max_length=50)
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  category=models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
  your_story=HTMLField()
  business_mail=models.CharField(max_length=100, default='kim@gmail.com')

  def __str__(self):
    return self.name
  def save_business(self):
    self.save()
  def delete_business(self):
    self.delete()

  @classmethod
  def search_business(cls,search_name):
    results = cls.objects.filter(name__icontains=search_name)
    return results
