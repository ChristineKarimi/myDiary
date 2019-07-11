from django import forms
from .models import Neighborhood,NeighborProfile,Business

class NewHoodForm(forms.ModelForm):
  class Meta:
    model=Neighborhood
    fields ='__all__'

class NewProfileForm(forms.ModelForm):
  class Meta:
    model=NeighborProfile
    exclude=['user']
  
class NewBusinessForm(forms.ModelForm):
  class Meta:
    model=Business
    exclude=['user']