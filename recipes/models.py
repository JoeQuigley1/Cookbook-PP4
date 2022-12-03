from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class SubmitRecipe(models.Model):
    recipe_name = models.CharField(
        max_length=50, unique=True, null=False, blank=False)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, blank=False)
    cook = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipe_post')
    description = models.TextField()
    recipe_image = CloudinaryField('image', null=False, blank=False)
    status = models.IntegerField(choices=STATUS, default=0)
    difficulty = models.IntegerField(null=False, blank=False)
    likes = models.ManyToManyField(
        User, related_name='recipe_likes', blank=True),
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ['-created_on']

    def __str__(self):

        return self.recipe_name

    def number_of_likes(self):

        return self.likes.count()