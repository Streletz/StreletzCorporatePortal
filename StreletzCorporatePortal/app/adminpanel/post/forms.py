import datetime

from django import forms
from django.forms import ModelChoiceField

from app.models import Department, Employee, Post


class DepartmentModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class BootstrapPostCreateForm(forms.ModelForm):
    """Post create form which uses boostrap CSS."""
    theme = forms.CharField(max_length=255, label='Тема',
                            widget=forms.TextInput({
                                'class': 'form-control'
                            }))
    # created = forms.DateField(initial=datetime.datetime.now(), widget=forms.HiddenInput)
    # author = forms.IntegerField(initial=0, widget=forms.HiddenInput)
    content = forms.CharField(label='Текст новости',
                              widget=forms.Textarea({
                                  'class': 'form-control'
                              }))

    class Meta:
        model = Post
        fields = ['theme', 'content']


class BootstrapPostEditForm(forms.ModelForm):
    """Post edit form which uses boostrap CSS."""
    id = forms.HiddenInput()
    theme = forms.CharField(max_length=255, label='Тема',
                            widget=forms.TextInput({
                                'class': 'form-control'
                            }))
    # created = forms.DateField(initial=datetime.datetime.now(), widget=forms.HiddenInput)
    # author = forms.IntegerField(initial=0, widget=forms.HiddenInput)
    content = forms.CharField(label='Текст новости',
                              widget=forms.Textarea({
                                  'class': 'form-control'
                              }))

    class Meta:
        model = Post
        fields = ['id', 'theme', 'content']


class BootstrapPostDeleteForm(forms.ModelForm):
    """Post create form which uses boostrap CSS."""
    id = forms.HiddenInput()
    theme = forms.CharField(max_length=255, label='Тема',
                           widget=forms.TextInput({
                               'class': 'form-control',
                               'readonly': True
                           }))

    class Meta:
        model = Department
        fields = ['id', 'theme']
