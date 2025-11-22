from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Course, Enrollment, Instructor, Payment, Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(
        choices=[('student', 'Student'), ('teacher', 'Teacher')],
        widget=forms.Select(attrs={
            'class': 'form-control role-select',
            'style': (
                'background-color:#f9f9f9; '
                'width:250px; '
                'padding:8px; '
                'border:1px solid #ccc; '
                'border-radius:6px; '
                'box-shadow:inset 0 1px 3px rgba(0,0,0,0.1); '
                'font-size:14px; '
                'color:#333; '
                'transition:all 0.3s ease;'
            )
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']
        help_texts = {
            'username': None,
            'email': None,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Profile.objects.create(user=user, role=self.cleaned_data['role'])
        return user


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'firstname', 'lastname', 'birthdate', 'email']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_id', 'course_name', 'course_description', 'credits', 'instructor_name']


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        # ✅ updated to match model: student, course
        fields = ['enrollment_id', 'student', 'course', 'status']


class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        # ✅ updated to match model: email not e_mail
        fields = ['instructor_id', 'first_name', 'last_name', 'email', 'department']


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        # ✅ updated to match model: student not student_id
        fields = ['payment_id', 'student', 'amount', 'payment_date', 'payment_method']