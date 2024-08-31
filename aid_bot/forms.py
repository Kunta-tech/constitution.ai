from django import forms

class SentenceForm(forms.Form):
    sentence = forms.CharField(
        label='Enter a sentence',
        widget=forms.Textarea(attrs={
            'placeholder': 'Type your sentence here...',
            'rows': 3,
            'cols': 40,
        }),
        max_length=1000,
    )