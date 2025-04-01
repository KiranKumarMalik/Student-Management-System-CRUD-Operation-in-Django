from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

from .models import Student
from .forms import StudentForm, StudentFilterForm


# Create your views here.
def index(request):
    students = Student.objects.all().order_by('id')  # Order by ID
    form = StudentFilterForm(request.GET)  # Get filter values from URL parameters

    # Apply filters if valid data is present
    if form.is_valid():
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        student_number = form.cleaned_data.get('student_number')
        gender = form.cleaned_data.get('gender')
        email = form.cleaned_data.get('email')
        course = form.cleaned_data.get('course')
        field_of_study = form.cleaned_data.get('field_of_study')
        min_gpa = form.cleaned_data.get('min_gpa')
        max_gpa = form.cleaned_data.get('max_gpa')

        # Apply filters dynamically
        if first_name:
            students = students.filter(first_name__icontains=first_name)
        if last_name:
            students = students.filter(last_name__icontains=last_name)
        if student_number:
            students = students.filter(student_number=student_number)
        if gender:
            students = students.filter(gender=gender)
        if email:
            students = students.filter(email__icontains=email)
        if course:
            students = students.filter(course=course)
        if field_of_study:
            students = students.filter(field_of_study__icontains=field_of_study)
        if min_gpa is not None:
            students = students.filter(gpa__gte=min_gpa)
        if max_gpa is not None:
            students = students.filter(gpa__lte=max_gpa)

    # Paginate results (10 students per page)
    paginator = Paginator(students, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'students/index.html', {'page_obj': page_obj, 'form': form})


def view_student(request, id):
  return HttpResponseRedirect(reverse('index'))


def add(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      new_student_number = form.cleaned_data['student_number']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_email = form.cleaned_data['email']
      course_name = form.cleaned_data['course']
      new_field_of_study = form.cleaned_data['field_of_study']
      new_gpa = form.cleaned_data['gpa']
      new_gender = form.cleaned_data['gender']

      new_student = Student(
        student_number=new_student_number,
        first_name=new_first_name,
        last_name=new_last_name,
        email=new_email,
        course=course_name,
        field_of_study=new_field_of_study,
        gpa=new_gpa,
        gender=new_gender
      )
      new_student.save()
      return render(request, 'students/add.html', {
        'form': StudentForm(),
        'success': True
      })
  else:
    form = StudentForm()
  return render(request, 'students/add.html', {
    'form': StudentForm()
  })


def edit(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'students/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'students/edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
    messages.success(request, f"Student {student.first_name} {student.last_name} has been deleted successfully.")
  return HttpResponseRedirect(reverse('index'))
