"""NewsAggregator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name = "landing"),
     path('index/', views.index, name = "index"),
     path('serach/', views.serach, name = "serach"),
    path('serachbar/',views.serachbar,name="serachbar"),
    path('categorey/',views.categorey,name="categorey"),
    path('prediction/',views.prediction,name="prediction"),
    path('predict/',views.predict,name="predict"),
    path('topnews/',views.topnews,name="topnews"),
    path('sports/',views.sports,name="sports"),
    path('health/',views.health,name="health"),
    path('auto/',views.auto,name="auto"),
    path('space/',views.space,name="space"),
    path('political/',views.political,name="political"),
    
    
]
