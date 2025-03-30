from django.db import models


# Create your models here.
class Student(models.Model):
  GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
  student_number = models.PositiveIntegerField()
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  course = models.CharField(max_length=100,default="Unknown Course")
  field_of_study = models.CharField(max_length=50)
  gpa = models.FloatField()
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

  def __str__(self):
    return f'Student: {self.first_name} {self.last_name}'
