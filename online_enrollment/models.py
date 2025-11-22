from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    # Link each student to a Django User
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile", null=True, blank=True)
    student_id = models.CharField(max_length=100, unique=True)
    firstname = models.CharField(max_length=100, default="")
    lastname = models.CharField(max_length=100, default="")
    birthdate = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.student_id} - {self.firstname} {self.lastname}"


class Course(models.Model):
    course_id = models.CharField(max_length=100, unique=True)
    course_name = models.CharField(max_length=100, default="")
    course_description = models.TextField(blank=True, default="")
    credits = models.IntegerField(default=0)
    instructor_name = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return f"{self.course_id} - {self.course_name}"


class Enrollment(models.Model):
    enrollment_id = models.CharField(max_length=100, unique=True)
    # Proper foreign keys
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments', default="")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments', default="")
    enrollment_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100, default="pending")

    def __str__(self):
        return f"{self.enrollment_id} ({self.student} -> {self.course})"


class Instructor(models.Model):
    instructor_id = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    email = models.EmailField(blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return f"{self.instructor_id} - {self.first_name} {self.last_name}"


class Payment(models.Model):
    payment_id = models.CharField(max_length=100, unique=True)
    # Link payment to Student instead of plain text
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='payments', default="")
    amount = models.FloatField(default=0.0)
    payment_date = models.DateField(null=True, blank=True)
    payment_method = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return f"{self.payment_id} ({self.student})"


class Profile(models.Model):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="student")

    def __str__(self):
        return f"{self.user.username} - {self.role}"