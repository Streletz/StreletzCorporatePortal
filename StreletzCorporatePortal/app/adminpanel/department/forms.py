from django import forms
from django.forms import ModelChoiceField

from app.models import Department, Employee


class DepartmentModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


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
    director = DepartmentModelChoiceField(
        queryset=None,
        required=False,
        label='Руководитель')

    class Meta:
        model = Department
        fields = ['id', 'name', 'description']

    def __init__(self, *args, **kwargs):
        # Only in case we build the form from an instance
        # (otherwise, 'toppings' list should be empty)
        forms.ModelForm.__init__(self, *args, **kwargs)
        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            department = kwargs['instance']
            director = None
            if department.director_set.filter(employee__isActive=True).count() > 0:
                director = department.director_set.filter(employee__isActive=True).first().employee
            director_field = self.fields['director']
            director_field.queryset = Employee.objects.filter(department_id=department.id).filter(
                isActive=True).all()
            director_field.initial = director.id if director is not None else 0


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
