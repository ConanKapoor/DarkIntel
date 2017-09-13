#Author - Shivam Kapoor

#Importing Essentials
from django.conf.urls import url
from Frontend import views

#Forming URLs
urlpatterns = [
    url(r'^$', views.darkintel_retrieval, name='darkintel'),
]
