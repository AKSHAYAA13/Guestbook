from django.db import models

# Create your models here.
# models.py

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bookname = models.CharField(max_length=200)
    feedback = models.TextField()

    def __str__(self):
        return self.name
