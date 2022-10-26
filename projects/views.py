from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from projects.forms import ProjectForm
from django.contrib.auth.decorators import login_required


@login_required
def list_projects(request):
    list_projects = Project.objects.filter(owner=request.user)
    context = {"Project": list_projects}
    return render(request, "projects/list.html", context)


@login_required
def show_project(request, id):
    projects = get_object_or_404(Project, id=id)
    context = {
        "project_object": projects,
    }
    return render(request, "proejcts/detail.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.purchaser = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()

        context = {
            "form": form,
        }
        return render(request, "projects/create.html", context)
