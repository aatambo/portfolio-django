from django.db import models


class Project(models.Model):
    """
    creates a model 'project'
    """

    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    github = models.URLField()
    project_url = models.URLField(blank=True)
    image = models.ImageField(upload_to="media/uploads/")
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.title
