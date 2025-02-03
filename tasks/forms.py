from django import forms 

class TaskForm(forms.Form):
    description = forms.CharField(max_length=255, required=True, label="Descripcion")