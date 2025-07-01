from django.db import models

class VideoTutorial(models.Model):
    language = models.CharField(max_length=50)
    page = models.TextField()

    def __str__(self):
        return f"{self.language}"

class Certificate(models.Model):
    name = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    completion_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.course}"

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

class Tutorials(models.Model):
    title = models.CharField(max_length=50)
    details = models.TextField()

    def __str__(self):
        return self.title