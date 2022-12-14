from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f'{self.title}'
