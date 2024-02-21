from django import forms
from django.forms import ModelForm
from a_posts.models import *


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ["url", "body"]
        labels = {"body": "Caption"}
        widgets = {
            "body": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Add a caption ...",
                    "class": "font1 text-4xl",
                },
            ),
            "url": forms.TextInput(
                attrs={
                    "placeholder": "Add a url ...",
                },
            ),
        }


class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ["body"]
        labels = {"body": ""}
        widgets = {
            "body": forms.Textarea(
                attrs={
                    "rows": 3,
                    "class": "font1 text-4xl",
                },
            ),
        }