from django.urls import path
from catalog.apps import CatalogConfig
from contacts.views import contacts
app_name = CatalogConfig.name



urlpatterns = [
    path('', contacts, name='contacts'),
]
