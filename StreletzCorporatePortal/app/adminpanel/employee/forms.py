from django import forms
from django.forms import ModelChoiceField

from app.models import Department, Employee, Position


class EmployeeDateInput(forms.DateInput):
    input_type = 'date'
    format = '%Y-%m-%d'


class EmployeeModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class BootstrapEmployeeCreateForm(forms.ModelForm):
    """Employee create form which uses boostrap CSS."""
    name = forms.CharField(max_length=255, label='ФИО', required=True,
                           widget=forms.TextInput({
                               'class': 'form-control'
                           }))
    birthday = forms.DateField(label='Дата рождения', required=True,
                               widget=EmployeeDateInput({
                                   'class': 'form-control'
                               }))
    worksSince = forms.DateField(label='Работает с', required=True,
                                 widget=EmployeeDateInput({
                                     'class': 'form-control'
                                 }))
    department = EmployeeModelChoiceField(queryset=Department.objects.all(), required=True,
                                          label='Подразделение', widget=forms.Select(attrs={'class': 'form-control'}))
    position = EmployeeModelChoiceField(queryset=Position.objects.all(), required=True,
                                        label='Должность', widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Employee
        fields = ['name', 'birthday', 'worksSince', 'department', 'position']


class BootstrapEmployeeEditForm(forms.ModelForm):
    """Employee edit form which uses boostrap CSS."""
    id = forms.HiddenInput()
    name = forms.CharField(max_length=255, label='ФИО', required=True,
                           widget=forms.TextInput({
                               'class': 'form-control'
                           }))
    birthday = forms.DateField(label='Дата рождения', required=True, input_formats=['%y-%m-%d'],
                               widget=EmployeeDateInput({
                                   'class': 'form-control'
                               }))
    worksSince = forms.DateField(label='Работает с', required=True,
                                 widget=EmployeeDateInput({
                                     'class': 'form-control'
                                 }))
    isActive = forms.BooleanField(label="Работает", required=False,
                                  widget=forms.CheckboxInput({'class': 'form-check-input'}))
    dismissed = forms.DateField(label='Уволен', required=False,
                                widget=EmployeeDateInput({
                                    'class': 'form-control'
                                }))
    department = EmployeeModelChoiceField(queryset=Department.objects.all(), required=True,
                                          label='Подразделение', widget=forms.Select(attrs={'class': 'form-control'}))
    position = EmployeeModelChoiceField(queryset=Position.objects.all(), required=True,
                                        label='Должность', widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Employee
        fields = ['name', 'birthday', 'worksSince', 'isActive', 'dismissed', 'department', 'position']


class BootstrapEmployeeDeleteForm(forms.ModelForm):
    """Employee create form which uses boostrap CSS."""
    name = forms.CharField(max_length=255, label='ФИО',
                           widget=forms.TextInput({
                               'class': 'form-control',
                               'readonly': True
                           }))

    class Meta:
        model = Employee
        fields = ['id', 'name']
