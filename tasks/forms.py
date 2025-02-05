from django import forms 

class TaskForm(forms.Form):
    description = forms.CharField(max_length=255, required=True, label="Descripcion")

    def clean_description(self):
        description = self.cleaned_data ['description']
        description = description.lower()
        if 'matematicas' in description:
            raise forms.ValidationError('NO acepta matematicas')
        
        return description