from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
from comments.models import Comment


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.CharField(max_length=360)
    created_at = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(null=True, blank=True)
    likes = models.IntegerField(default=0)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text




class Document(models.Model):
    docfile = models.FileField(upload_to='document/%y/%m/%d')

    # store file in media/documents/2017/03/30
    def upload(self):
        self.save()

    def __str__(self):
        return self.docfile.path


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Article(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=65000)
    timestamp = models.DateTimeField(default=timezone.now)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    comments=models.IntegerField(default=0)
    banner = models.ImageField(upload_to=upload_location,
                               null=True,
                               blank=True,
                               width_field="width_field",
                               height_field="height_field")
    category = models.CharField(max_length=20,
                                choices=(("html", "html"),
                                         ("css", "css"),
                                         ("js", "javascript"),
                                         ("all", "Other")))

    def upload(self):
        self.save()

    def get_absolute_url(self):
        return reverse("details", kwargs={"id": self.id})

    class Meta:
        ordering = ["timestamp"]
