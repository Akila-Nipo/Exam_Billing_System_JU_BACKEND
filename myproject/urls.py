from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('day4app/',include('day4app.urls')),
    
  
]
