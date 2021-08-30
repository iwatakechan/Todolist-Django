from django.db import models

CHOICE = (('danger', 'high'),('warning', 'normal'),('primary', 'low'))

class Todo(models.Model):
    title = models.CharField(max_length=200)
    memo = models.TextField()
    priority = models.CharField(
      max_length=50,
      choices = CHOICE
      )
    createdate = models.DateField()

    def __str__(self):
      return self.title
