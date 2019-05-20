from django.db import models
from django.utils import timezone

# Create your models here.
class Poat (models.Model):
    authot = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def published(self):
        self.published_date = timezone.now()

    def __str__(self):
        return  self.title
