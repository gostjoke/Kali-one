from django.db import models

# Create your models here.
class ExampleModel(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name