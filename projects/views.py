from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project


# Create your views here.
def list_projects(request):
    list_projects = Project.objects.all()
    context = {"Project": list_projects}
    return render(request, "projects/list.html", context)
