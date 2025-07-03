from django.shortcuts import render, get_object_or_404
from .models import Projects
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.

def index(request):
    featured_projects = Projects.objects.filter(project_feature=True)[:3]
    return render(request, "portfolio/index.html", {"featured_projects": featured_projects})


def project_detail(request, slug):
    project = get_object_or_404(Projects, project_slug=slug)
    return render(request, "portfolio/project_detail.html", {"project": project})


def all_projects(request):
    projects = Projects.objects.all()
    return render(request, "portfolio/all_projects.html", {"projects": projects})
