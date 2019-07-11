
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Neighborhood,NeighborProfile,Business
from django.contrib.auth.decorators import login_required
from .forms import NewHoodForm,NewProfileForm,NewBusinessForm
# Create your views here.

def home(request):
  hoods=Neighborhood.objects.all()
  title = 'Our Hood'
  return render(request,'home.html',{"title":title,"hoods":hoods})

@login_required(login_url='/accounts/login')
def hoods(request,neighborhood_id):
 
  try:
    hood = Neighborhood.objects.filter(id=neighborhood_id)
    found = Business.objects.filter(neighborhood=neighborhood_id)[0:1]
  except DoesNotExist:
    raise Http404() 

  return render(request,'hood.html',{"hood":hood,"found":found})

def user_profile(request):
  current_user = request.user
  profiles= NeighborProfile.objects.filter(user=current_user)[0:1]

  return render(request,'profile.html',{"profiles":profiles})

@login_required(login_url='/accounts/login')
def new_hood(request):
  current_user = request.user 
  if request.method == 'POST':
    form = NewHoodForm(request.POST,request.FILES)
    if form.is_valid():
      hood = form.save(commit=False)
      hood.user = current_user
      hood.save()
    return redirect('home')
  else:
    form=NewHoodForm()
    return render(request,'new_hood.html',{"form":form})

@login_required(login_url='/accounts/login')
def new_neighbour(request):
  current_user =  request.user 
  if request.method == 'POST':
    form = NewProfileForm(request.POST,request.FILES)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = current_user
      prof_pic=form.cleaned_data['prof_pic']
      name=form.cleaned_data['name']
      email= form.cleaned_data['email']
      NeighborProfile.objects.filter(user=current_user).update(prof_pic=prof_pic,name=name,email=email)
      profile.save()       
    return redirect('userProfile')

  else:
    form=NewProfileForm()
    return render(request,'new_neighbor.html',{"form":form})

@login_required(login_url='/accounts/login')
def new_business(request):
  current_user=request.user
  if request.method == 'POST':
    form = NewBusinessForm(request.POST,request.FILES)
    if form.is_valid():
      business = form.save(commit=False)
      business.user = current_user
      business.save()
    return redirect ('home')
  else:
    form = NewBusinessForm()
    return render(request,'new_business.html',{"form":form})

def search_business(request):
  if 'name' in request.GET and request.GET['name']:
    search_name = request.GET.get('name')
    business_found = Business.search_business(search_name)[0:1]
    
    message = f'{search_name}'

    return render(request,'search.html',{"message":message, "businesses":business_found})

  else:
    message = "Try retyping the name again."
    return render(request,'search.html',{"message":message})
