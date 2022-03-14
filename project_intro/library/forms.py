from django import forms
from .models import BookReview


class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ('content', 'book', 'reviewer', )
        widgets = {
            'book': forms.HiddenInput(),
            'reviewer': forms.HiddenInput(),
            'content': forms.Textarea(),
        }
