from django.db import models

# Create your models here.
class Task(models.Model):
    CATEGORY_CHOICES = [
        ('work', 'Work'),
        ('personal', 'Personal'),
        ('shopping', 'Shopping'),
        ('other', 'Other'),
    ]
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    priority = models.IntegerField(choices=PRIORITY_CHOICES)

    def __str__(self):
        return self.title