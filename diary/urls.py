from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  url(r'^$',views.home,name='home'),
  url(r'^accounts/',include('registration.backends.simple.urls')),
  url(r'^post-details/(?P<neighborhood_id>[0-9])$',views.hoods,name='post-details'),
  url(r'^new/newPost$',views.new_hood,name='newPost'),
  url(r'^new/neighbour$',views.new_neighbour,name='newDiaryEntry'),
  url(r'^new/newDiaryPost$',views.new_business,name='newDiaryPost'),
  url(r'^profile/',views.user_profile,name='userProfile'),
  url(r'^search/',views.search_business,name='search'),
]

if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)