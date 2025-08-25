from django.db import models

class BlogAuthor(models.Model):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='authors/')

    def __str__(self):
        return self.full_name


class BlogModel(models.Model):
    image = models.ImageField(upload_to='recipes/')
    category = models.CharField(max_length=128)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


    author = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True)


    updated_ad = models.DateTimeField(auto_now=True)
    created_ad = models.DateTimeField(auto_now_add=True)

class CommentModel(BlogAuthor):
    text = models.CharField(max_length=255)
    author = models.ForeignKey(BlogAuthor, on_delete=models.CASCADE, null=False, related_name="comments")
    category = models.CharField(max_length=128)

    updated_ad = models.DateTimeField(auto_now=True)
    created_ad = models.DateTimeField(auto_now_add=True)