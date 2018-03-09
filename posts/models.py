from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    img = models.FileField(upload_to='public/uploads/')

    def imgName(self):
        return self.img.name[7:]
