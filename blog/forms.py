from .models import Comment, Recipe
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


# class SubmitRecipe(forms.ModelForm):

#     class Meta:
#         model = Recipe
#         fields = (
#             'body',
#             'slug',
#             'description',
#             'featured_image',
#         )
