from django import forms 
from .models import Task

class TaskForm(forms.Form):
    description = forms.CharField(max_length=255, required=True, label="Descripcion")

    def clean_description(self):
        description = self.cleaned_data ['description']
        description = description.lower()
        if 'matematicas' in description:
            raise forms.ValidationError('NO acepta matematicas')
        
        return description
    



class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description']
        labels = { 'description': 'Descripcion', }

    def clean_description(self):
        description = self.cleaned_data ['description']
        description = description.lower()
        if 'matematicas' in description:
            raise forms.ValidationError('NO acepta matematicas')
        
        return description    