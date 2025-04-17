from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_persons, name='create_persons'),
    path('update/<int:id>/', views.update_person, name='update_person'),
    path('delete/<int:id>/', views.delete_person, name='delete_person'),
]
