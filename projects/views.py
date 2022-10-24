from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def list_projects(request):
    list_projects = Project.objects.filter(owner=request.user)
    context = {"Project": list_projects}
    return render(request, "projects/list.html", context)
