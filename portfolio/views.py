from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from .models import Project


class ProjectView(ListView):
    """
    creates a view for projects
    """

    template_name = "index.html"
    model = Project
    context_object_name = "project"


class ProjectDetailView(DetailView):
    """
    creates a view for project details
    """

    template_name = "project_detail.html"
    model = Project
    context_object_name = "project-detail"
