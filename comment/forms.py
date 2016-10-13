from comment.models import Comment
from django import forms


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = [
            'author',
            'email',
            'content',
        ]
        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Nick'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'content': forms.Textarea(attrs={'placeholder': 'Comment...'}, ),
        }
