from django import forms
from app.models import Department


class BootstrapDepartmentCreateForm(forms.ModelForm):
    """Department create form which uses boostrap CSS."""
    name = forms.CharField(max_length=255, label='Название',
                           widget=forms.TextInput({
                               'class': 'form-control'
                           }))
    description = forms.CharField(max_length=255, label='Описание',
                                  widget=forms.Textarea({
                                      'class': 'form-control'
                                  }))

    class Meta:
        model = Department
        fields = ['name', 'description']


class BootstrapDepartmentEditForm(forms.ModelForm):
    """Department edit form which uses boostrap CSS."""
    id = forms.HiddenInput()
    name = forms.CharField(max_length=255, label='Название',
                           widget=forms.TextInput({
                               'class': 'form-control'
                           }))
    description = forms.CharField(max_length=255, label='Описание',
                                  widget=forms.Textarea({
                                      'class': 'form-control'
                                  }))

    class Meta:
        model = Department
        fields = ['id', 'name', 'description']


class BootstrapDepartmentDeleteForm(forms.ModelForm):
    """Department create form which uses boostrap CSS."""
    name = forms.CharField(max_length=255, label='Название',
                           widget=forms.TextInput({
                               'class': 'form-control',
                               'readonly': True
                           }))

    class Meta:
        model = Department
        fields = ['id', 'name']
