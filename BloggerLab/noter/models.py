from django.db import models

# Create your models here.

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", default='images/default.jpg')
    files = models.FileField(upload_to="misc/",default="misc/default.txt")