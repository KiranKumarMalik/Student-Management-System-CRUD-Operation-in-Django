from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Student(models.Model):
  GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
  COURSE_CHOICES = [
        ('BTECH', 'Bachelors in Technology'),
        ('MTECH', 'Masters in Technology'),
        ('Bachelors', 'Bachelors'),
        ('Masters', 'Masters'),
        ('Diploma', 'Diploma'),
        ('ITI', 'ITI'),
    ]
  student_number = models.PositiveIntegerField(unique=True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  course = models.CharField(max_length=100, choices=COURSE_CHOICES, default="BTECH")
  field_of_study = models.CharField(max_length=50)
  gpa = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

  def __str__(self):
    return f'Student: {self.first_name} {self.last_name}'
