from django import forms
from .models import FooterVragenModel

class FooterVragenForm(forms.ModelForm):
    class Meta:
        model = FooterVragenModel
        fields = ['category', 'question']
        widgets = {
            'question': forms.Textarea(attrs={
                'rows': 15,
                'maxlength': 1000
            })
        }

    def __init__(self, *args, **kwargs):
        super(FooterVragenForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = None 
        
        choices_list = list(self.fields['category'].choices)
        self.fields['category'].choices = [('', 'Kies een onderwerp')] + choices_list[1:]

