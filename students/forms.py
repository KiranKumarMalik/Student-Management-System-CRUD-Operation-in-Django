from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['student_number', 'first_name', 'last_name', 'email', 'course', 'field_of_study', 'gpa', 'gender']
    labels = {
      'student_number': 'Student Number',
      'first_name': 'First Name',
      'last_name': 'Last Name',
      'email': 'Email',
      'course': 'Course',
      'field_of_study': 'Field of Study',
      'gpa': 'CGPA',
      'gender': 'Gender'
    }
    widgets = {
      'student_number': forms.NumberInput(attrs={'class': 'form-control'}),
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'course': forms.Select(attrs={'class': 'form-control', 'id': 'course-select'}),
      'field_of_study': forms.Select(attrs={'class': 'form-control', 'id': 'field-select'}),
      'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
      'gender': forms.Select(attrs={'class': 'form-control'}),
    }

class StudentFilterForm(forms.Form):
    first_name = forms.CharField(required=False, label="First Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=False, label="Last Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    student_number = forms.IntegerField(required=False, label="Registration Number", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(choices=[('', 'All Gender')] + Student.GENDER_CHOICES, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False, label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    course = forms.ChoiceField(choices=[('', 'All Courses')] + Student.COURSE_CHOICES, required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    field_of_study = forms.CharField(required=False, label="Field of Study", widget=forms.TextInput(attrs={'class': 'form-control'}))
    min_gpa = forms.FloatField(required=False, label="Min CGPA", widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '10', 'step': '0.1'}))
    max_gpa = forms.FloatField(required=False, label="Max CGPA", widget=forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '10', 'step': '0.1'}))

