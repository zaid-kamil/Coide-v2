from django.db import models
from django.urls import reverse
from django.utils import timezone


class CodeScript(models.Model):
    creator = models.ForeignKey('auth.User')
    title = models.CharField(max_length=25)
    #banner = models.FileField(upload_to='codescript/%y/%m/%d')
    html_file_path = models.TextField(max_length=255)
    css_file_path = models.TextField(max_length=255)
    js_file_path = models.TextField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(default=timezone.now)
    stars = models.IntegerField(default=0)

    def upload(self):
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("codescript", kwargs={"id": self.id})

    class Meta:
        ordering = ["-created_at"]


# Create your models here.
