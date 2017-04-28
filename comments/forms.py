from django import forms

from comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content", "article_id"]
        widgets = {
            "content": forms.Textarea(),
            "article_id": forms.HiddenInput()
        }
