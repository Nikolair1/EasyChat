from django.db import models
from django.core.validators import MinLengthValidator

# Constants
MAX_NAME = 50
MAX_MSG = 250


class User(models.Model):
    name = models.CharField(
        max_length=MAX_NAME, unique=True, validators=[MinLengthValidator(1)]
    )
    color = models.CharField(max_length=7, default="#000000")  # Default color is black

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} : {self.message}"
