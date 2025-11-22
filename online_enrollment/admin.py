from django.contrib import admin
from .models import Student, Course, Enrollment, Instructor, Payment

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Instructor)
admin.site.register(Payment)

# Register your models here.
