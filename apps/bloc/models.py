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



class BlocAuthorModel(models.Model):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='authors/', blank=True)


    def __str__(self):
        return self.full_name



class BlocCategoryModel(models.Model):
    title = models.CharField(max_length=255)

class BlocTagModel(models.Model):
    title = models.CharField(max_length=255)

class BlogsModel(models.Model):
    image = models.ImageField(upload_to='recipes/', blank=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()

    updated_ad = models.DateTimeField(auto_now=True)
    created_ad = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(BlocAuthorModel, on_delete=models.CASCADE, null=False, related_name="autor_model")
    category = models.ManyToManyField(BlocCategoryModel , related_name="category_model")
    tag = models.ManyToManyField(BlocTagModel, related_name="tag_model")

    status = models.BooleanField(default=False, blank=False)

    class Meta:
        verbose_name = 'bloc_model'
        verbose_name_plural = 'bloc_models  '


class BlogComentaryModel(models.Model):
    title = models.CharField(max_length=255)
    blog = models.ForeignKey(BlogsModel, on_delete=models.CASCADE, null=False, related_name="comment_model")

    updated_ad = models.DateTimeField(auto_now=True)
    created_ad = models.DateTimeField(auto_now_add=True)