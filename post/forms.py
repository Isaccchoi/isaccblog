from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Post
from .models import Category


class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False,
                            label="태그")

    class Meta:
        model = Post
        fields = ("category", "title", "content", "active", )
        labels = {
            "category": _("카테고리"),
            "title": _("제목"),
            "content": _("내용"),
            "active": _("배포"),
        }
