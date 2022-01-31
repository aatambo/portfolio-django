from django.urls import path

from .views import ProjectDetailView, ProjectView

urlpatterns = [
    path("", ProjectView.as_view(), name="project-index"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
]
