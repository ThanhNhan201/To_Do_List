from django.db import models

# Create your models here.

class ListDo(models.Model):
    order = models.IntegerField(default=0)
    color_bg = models.CharField(default="fff",blank=True, max_length=6)
    content = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    removed = models.BooleanField(default=False)


    class Meta:
        ordering = ["order"]

    # def __str__(self):
    #     return self.order