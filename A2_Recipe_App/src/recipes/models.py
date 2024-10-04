from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField(default='No ingredients provided')  # Add a default value
    cooking_time = models.IntegerField()
    difficulty = models.CharField(max_length=50)

    def __str__(self):
        return self.title
