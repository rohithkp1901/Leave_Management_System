from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('studentRegistration/',views.s_insert,name='studentRegistration'),
    path('s_login/',views.s_login,name='s_login'),
    path('s_login_view/',views.s_login_view,name='s_login_view'),
    path('s_logout_view/',views.s_logout_view,name='s_logout_view'),
    path('view_student_details/',views.view_student_details,name='view_student_details'),
    path('s_edit_profile/<str:username>',views.s_edit_profile,name='s_edit_profile'),
    path('add_leave_request/',views.add_leave_request,name='add_leave_request'),
    path('view_leave_requests/',views.view_leave_requests,name='view_leave_requests'),
    path('t_register/',views.register_teacher,name='t_register'),
    path('t_login/',views.t_login,name='t_login'),
    path('login_teacher/',views.login_teacher,name='login_teacher'),
    path('t_dashboard/',views.t_dashboard,name='t_dashboard'),
    path('not_approved/',views.not_approved,name='not_approved'),
    path('view_students/', views.view_students, name='view_students'),
    path('teacher_logout/', views.logout_user, name='teacher_logout'),
    path('approve_leave/<str:student_username>/',views.approve_leave, name='approve_leave'),
     path('pending_requests/', views.pending_requests, name='pending_requests'),
    path('view_student_request/<str:student_username>/', views.view_student_request, name='view_student_request'),



]
