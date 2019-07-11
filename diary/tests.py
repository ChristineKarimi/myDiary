from django.test import TestCase
from .models import Neighborhood,NeighborProfile,Business
# Create your tests here.

class HoodTestClass(TestCase):
  def setUp(self):    
    
    self.parklands = Neighborhood(name='Parklands',hood_image='parklands.jpg',members='5')
    self.parklands.save()
    
    self.jem = NeighborProfile(name='Jemila',email='njemila.306@gmail.com',prof_pic='Beauty.jpeg',user=self.jem,neighborhood=self.parklands)
    self.jem.save()

    self.gym = Business(description ='Spacious and well aerated. Full of energy and good vibes',name='Everything Check',business_mail='every.check@gym.com',user=self.jem,neighborhood=self.parklands)
    self.gym.save()
    
  #Testing instance
  def test_instance(self):
    self.assertTrue(isinstance(self.gym,Business))
    self.assertTrue(isinstance(self.jem,NeighborProfile))
    self.assertTrue(isinstance(self.parklands,Neighborhood))

  #Destroying the instance after test
  def tearDown(self):
    Business.object.all().delete()
    NeighborProfile.object.all().delete()
    Neighborhood.object.all().delete()