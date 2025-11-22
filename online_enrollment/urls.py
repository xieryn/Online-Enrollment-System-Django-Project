from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('', views.landing_page, name='landing_page'),
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/edit/', views.student_profile_edit, name='student_profile_edit'),

    # Students
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_add, name='student_add'),
    path('students/edit/<int:pk>/', views.student_edit, name='student_edit'),


    # Courses
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.course_add, name='course_add'),
    path('courses/edit/<int:pk>/', views.course_edit, name='course_edit'),

    # Enrollments
    path('enrollments/', views.enrollment_list, name='enrollment_list'),
    path('enrollments/add/', views.enrollment_add, name='enrollment_add'),
    path('enrollments/edit/<int:pk>/', views.enrollment_edit, name='enrollment_edit'),

    # Instructors
    path('instructors/', views.instructor_list, name='instructor_list'),
    path('instructors/add/', views.instructor_add, name='instructor_add'),
    path('instructors/edit/<int:pk>/', views.instructor_edit, name='instructor_edit'),

    # Payments
    path('payments/', views.payment_list, name='payment_list'),
    path('payments/add/', views.payment_add, name='payment_add'),
    path('payments/edit/<int:pk>/', views.payment_edit, name='payment_edit'),
]
