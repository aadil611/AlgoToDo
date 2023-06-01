from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ToDo(models.Model):
    OPEN    = "open"
    WORKING = "working"
    DONE    = "done"
    OVERDUE = "overdue"
    STATUS_CHOICES = (
        (OPEN, "Open"),
        (WORKING, "Working"),
        (DONE, "Done"),
        (OVERDUE, "Overdue"),
    )

    
    title         = models.CharField(max_length=100)
    description   = models.TextField(max_length=100)
    created_at    = models.DateField(auto_now_add=True)
    due_date      = models.DateField(blank=True, null=True)
    status        = models.CharField(choices=STATUS_CHOICES, default=OPEN, max_length=20)
    tags          = models.ManyToManyField(Tag, related_name="todos", blank=True)

    def __str__(self):
        return self.title