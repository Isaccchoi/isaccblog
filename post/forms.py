from django import forms
from .models import Post
from django.utils.translation import ugettext_lazy as _



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ("title", "content", "tags", "active", )
        labels = {
            "title": _("title"),
            "content": _("content"),
            "tags": _("tag"),
            "active": _("active"),
        }
