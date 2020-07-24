from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    due_date = models.DateField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
