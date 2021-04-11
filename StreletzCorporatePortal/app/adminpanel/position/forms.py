from django import forms
from app.models import Position


class BootstrapPositionCreateForm(forms.ModelForm):
    """Position create form which uses boostrap CSS."""
    name = forms.CharField(max_length=255, label='Название',
                           widget=forms.TextInput({
                               'class': 'form-control'
                           }))


    class Meta:
        model = Position
        fields = ['name']


class BootstrapPositionEditForm(forms.ModelForm):
    """Position edit form which uses boostrap CSS."""
    id = forms.HiddenInput()
    name = forms.CharField(max_length=255, label='Название',
                           widget=forms.TextInput({
                               'class': 'form-control'
                           }))

    class Meta:
        model = Position
        fields = ['id', 'name']


class BootstrapPositionDeleteForm(forms.ModelForm):
    """Position create form which uses boostrap CSS."""
    name = forms.CharField(max_length=255, label='Название',
                           widget=forms.TextInput({
                               'class': 'form-control',
                               'readonly': True
                           }))

    class Meta:
        model = Position
        fields = ['id', 'name']
