from django.db import models

DIFFICULTY_CHOICES = [
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard'),
]


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField(default='No ingredients provided')
    cooking_time = models.IntegerField()
    difficulty = models.CharField(max_length=6, choices=DIFFICULTY_CHOICES)
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)

    def __str__(self):
        return self.title
