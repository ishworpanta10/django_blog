from django.db import models
from django.utils import timezone
from django.urls import reverse


class Article(models.Model):
    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
