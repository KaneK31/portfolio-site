from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", views.all_projects, name="all_projects"),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),

]
