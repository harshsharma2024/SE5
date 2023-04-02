from django.urls import path
from . import views

urlpatterns=[
    path("",views.LandingPage,name="landingpage"),
    path("check/",views.check,name="check"),

    #User rooms
    path("teacher_room/",views.teacher_room,name="teacher-room"),
    path("student_room/",views.student_room,name="student-room"),


    #login-register users
    path("login_student/",views.StudentLogin,name="student-login"),
    path("register_student/",views.StudentRegister,name="student-register"),
    path("register_teacher/",views.TeacherRegister,name="teacher-register"),
    path("login_teacher/",views.TeacherLogin,name="teacher-login"),

    #functionality 
    path("join_room/",views.Join,name="join"),
    path("sactivity/",views.sactivity,name="sactivity"),
    path("students/",views.students,name="students"),
    path("sroom/<str:pk>/rstudents",views.rstudents,name="rstudents"),

    path('sroom/<str:pk>/',views.sroom,name="sroom"),
    path('create_room/',views.create_room,name='create-room'),
    path('logout_student/',views.LogOutStudent,name="logout-student"),
    path('logout_teacher/',views.LogOutTeacher,name="logout-teacher"),



]