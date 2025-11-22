
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import StudentForm, CourseForm, EnrollmentForm, InstructorForm, PaymentForm, RegisterForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, Student, Course, Enrollment, Instructor, Payment

# ---------------------------
# Course List
# ---------------------------

@login_required
def course_list(request):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')
    courses = Course.objects.all()
    return render(request, "course_list.html", {"courses": courses})

# ---------------------------
# Enrollment List
# ---------------------------

@login_required
def enrollment_list(request):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')
    enrollments = Enrollment.objects.all()
    return render(request, "enrollment_list.html", {"enrollments": enrollments})

# ---------------------------
# Instructor List
# ---------------------------

@login_required
def instructor_list(request):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')
    instructors = Instructor.objects.all()
    return render(request, "instructor_list.html", {"instructors": instructors})

# ---------------------------
# Payment List
# ---------------------------

@login_required
def payment_list(request):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')
    payments = Payment.objects.all()
    return render(request, "payment_list.html", {"payments": payments})

# ---------------------------
# Course Add/Edit
# ---------------------------

@login_required
def course_add(request):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added successfully!")
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, "course_form.html", {"form": form, "title": "Add Course"})

@login_required
def course_edit(request, pk):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, "course_form.html", {"form": form, "title": "Edit Course"})

# ---------------------------
# Enrollment Add/Edit
# ---------------------------

@login_required
def enrollment_add(request):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Enrollment added successfully!")
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()
    return render(request, "enrollment_form.html", {"form": form, "title": "Add Enrollment"})

@login_required
def enrollment_edit(request, pk):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == "POST":
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            messages.success(request, "Enrollment updated successfully!")
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm(instance=enrollment)
    return render(request, "enrollment_form.html", {"form": form, "title": "Edit Enrollment"})

# ---------------------------
# Instructor Add/Edit
# ---------------------------

@login_required
def instructor_add(request):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')
    if request.method == "POST":
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Instructor added successfully!")
            return redirect('instructor_list')
    else:
        form = InstructorForm()
    return render(request, "instructor_form.html", {"form": form, "title": "Add Instructor"})

@login_required
def instructor_edit(request, pk):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')
    instructor = get_object_or_404(Instructor, pk=pk)
    if request.method == "POST":
        form = InstructorForm(request.POST, instance=instructor)
        if form.is_valid():
            form.save()
            messages.success(request, "Instructor updated successfully!")
            return redirect('instructor_list')
    else:
        form = InstructorForm(instance=instructor)
    return render(request, "instructor_form.html", {"form": form, "title": "Edit Instructor"})

# ---------------------------
# Payment Add/Edit
# ---------------------------

@login_required
def payment_add(request):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Payment added successfully!")
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, "payment_form.html", {"form": form, "title": "Add Payment"})

@login_required
def payment_edit(request, pk):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == "POST":
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            messages.success(request, "Payment updated successfully!")
            return redirect('payment_list')
    else:
        form = PaymentForm(instance=payment)
    return render(request, "payment_form.html", {"form": form, "title": "Edit Payment"})
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import StudentForm, CourseForm, EnrollmentForm, InstructorForm, PaymentForm, RegisterForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, Student, Course, Enrollment, Instructor, Payment

# ---------------------------
# Auth & Landing Pages
# ---------------------------

def landing_page(request):
    return render(request, 'accounts/landing.html')

def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login_user')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_user(request):
    role = request.GET.get('role')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if role and role != user.profile.role:
                    messages.warning(request, f"You logged in as {user.profile.role}, not {role}. Redirecting...")
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form, 'role': role})

def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('landing_page')

# ---------------------------
# Dashboard & Profile
# ---------------------------

@login_required(login_url='login_user')
def dashboard(request):
    if request.user.profile.role == 'student':
        try:
            student = Student.objects.get(user=request.user)
        except Student.DoesNotExist:
            student = None
        return render(request, 'accounts/student_dashboard.html', {'student': student})
    elif request.user.profile.role == 'teacher':
        return render(request, 'accounts/teacher_dashboard.html')

@login_required
def profile_view(request):
    user = request.user
    context = {'user': user}
    if hasattr(user, 'profile') and user.profile.role == 'student':
        try:
            student = Student.objects.get(user=user)
        except Student.DoesNotExist:
            student = None
        enrollments = Enrollment.objects.filter(student=student) if student else []
        courses = Course.objects.filter(enrollments__student=student).distinct() if student else []
        instructors = Instructor.objects.filter(id__in=courses.values_list('instructor_name', flat=True)).distinct() if student else []
        payments = Payment.objects.filter(student=student) if student else []
        context.update({
            'student': student,
            'enrollments': enrollments,
            'courses': courses,
            'instructors': instructors,
            'payments': payments,
        })
    return render(request, 'profile.html', context)

# ---------------------------
# Students
# ---------------------------

@login_required
def student_list(request):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')
    
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})

@login_required
def student_add(request):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, "student_form.html", {"form": form, "title": "Add Student"})

@login_required
def student_edit(request, pk):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')

    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, "student_form.html", {"form": form, "title": "Edit Student"})


# ---------------------------
# Courses
# ---------------------------


# Course Add
@login_required
def course_add(request):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course added successfully!")
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, "course_form.html", {"form": form, "title": "Add Course"})

# Course Edit
@login_required
def course_edit(request, pk):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, "course_form.html", {"form": form, "title": "Edit Course"})

# ---------------------------
# Enrollments
# ---------------------------


# Enrollment Add
@login_required
def enrollment_add(request):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Enrollment added successfully!")
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()
    return render(request, "enrollment_form.html", {"form": form, "title": "Add Enrollment"})

# Enrollment Edit
@login_required
def enrollment_edit(request, pk):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == "POST":
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            messages.success(request, "Enrollment updated successfully!")
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm(instance=enrollment)
    return render(request, "enrollment_form.html", {"form": form, "title": "Edit Enrollment"})

# ---------------------------
# Instructors
# ---------------------------


# Instructor Add
@login_required
def instructor_add(request):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')
    if request.method == "POST":
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Instructor added successfully!")
            return redirect('instructor_list')
    else:
        form = InstructorForm()
    return render(request, "instructor_form.html", {"form": form, "title": "Add Instructor"})

# Instructor Edit
@login_required
def instructor_edit(request, pk):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')
    instructor = get_object_or_404(Instructor, pk=pk)
    if request.method == "POST":
        form = InstructorForm(request.POST, instance=instructor)
        if form.is_valid():
            form.save()
            messages.success(request, "Instructor updated successfully!")
            return redirect('instructor_list')
    else:
        form = InstructorForm(instance=instructor)
    return render(request, "instructor_form.html", {"form": form, "title": "Edit Instructor"})

# ---------------------------
# Payments
# ---------------------------


# Payment Add
@login_required
def payment_add(request):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Payment added successfully!")
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, "payment_form.html", {"form": form, "title": "Add Payment"})

# Payment Edit
@login_required
def payment_edit(request, pk):
    if request.user.profile.role != 'teacher':
        return redirect('dashboard')
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == "POST":
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            messages.success(request, "Payment updated successfully!")
            return redirect('payment_list')
    else:
        form = PaymentForm(instance=payment)
    return render(request, "payment_form.html", {"form": form, "title": "Edit Payment"})

# ---------------------------
# Student profile (own)
# ---------------------------

@login_required
def student_profile_edit(request):
    if request.user.profile.role != 'student':
        return redirect('dashboard')

    student, created = Student.objects.get_or_create(
        user=request.user,
        defaults={
            'firstname': request.user.first_name,
            'lastname': request.user.last_name,
            'email': request.user.email,
        }
    )

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile_view')
    else:
        form = StudentForm(instance=student)
    return render(request, "student_profile.html", {"form": form})

# ---------------------------
# Delete profile
# ---------------------------

@login_required
def student_profile_delete(request):
    if request.user.profile.role != 'student':
        return redirect('dashboard')

    student = get_object_or_404(Student, user=request.user)

    if request.method == "POST":
        student.delete()
        messages.success(request, "Your profile has been deleted.")
        return redirect('logout_user')

    return render(request, "confirm_delete.html", {"student": student})

# ---------------------------
# Signals
# ---------------------------

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if not created:
        instance.profile.save()
