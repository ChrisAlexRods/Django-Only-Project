from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm
from tasks.models import Task


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.purchaser = request.user
            task.save()
            return redirect("list_projects")
    else:
        form = TaskForm()

        context = {
            "form": form,
        }
        return render(request, "tasks/create.html", context)


@login_required
def list_task(request):
    list_task = Task.objects.filter(assignee=request.user)
    context = {"Task": list_task}
    return render(request, "tasks/list.html", context)
