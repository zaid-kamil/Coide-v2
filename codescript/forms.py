from django import forms

from codescript.models import CodeScript


class CodeForm(forms.ModelForm):
    class Meta:
        model = CodeScript
        fields = ["title","creator"]
        widgets = {
            "title": forms.TextInput(),
            "creator": forms.HiddenInput()
        }
