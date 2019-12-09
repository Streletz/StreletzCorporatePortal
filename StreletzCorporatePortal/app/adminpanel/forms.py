from django import forms
from app.models import Department



class BootstrapDepartmentForm(forms.ModelForm):
    """Authentication form which uses boostrap CSS."""
    name = forms.CharField(max_length=255,label='Название',
                               widget=forms.TextInput({
                                   'class': 'form-control'
                                   }))
    class Meta:
        model = Department
        fields = ['name']
        
  
