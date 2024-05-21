from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse



class Role(models.Model):
    Role_Choices = [
          ("product_owner", "Product Owner"),
          ("Developer", "Developer"),
          ("scrum_master", "Scrum Master"),
    ]
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    
class Team(models.Model):
        Team_Names = [
            ("alpha", "Alpha Squad"),
            ("beta", "Beta Squad"),
            ("charlie", "Charlie Squad"),
]
        name = models.CharField(max_length=128)
        description = models.CharField(max_length=256)

        def __str__(self):
            return self.name
        

class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Issue(models.Model):
    name = models.CharField(max_length=128)
    summary = models.CharField(max_length=256)
    description = models.TextField()
    reporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="reporter"
    )
    assignee = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="assignee"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("detail", args=[self.id])

    def __str__(self):
        return self.name
        
class CustomUser(AbstractUser):
            role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True)
            team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)