from django.urls import path
from core import views



urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('projects/<int:pk>/', views.ProjectView.as_view(), name='project_detail'),
    path('contact', views.ContactView.as_view(), name='contact')
]
