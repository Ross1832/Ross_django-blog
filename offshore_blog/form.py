from django import forms
from mptt.forms import TreeNodeChoiceField

from .models import Comment


class CommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['parent'].widget.attrs.update({'class': 'd-none'})
        # self.fields['parent'].label = ''
        self.fields['parent'].required = False

    class Meta:
        model = Comment
        fields = (
            'name',
            'parent',
            'content',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'parent': forms.IntegerField(attrs={}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
