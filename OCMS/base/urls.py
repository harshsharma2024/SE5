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
    path("tactivity/",views.tactivity,name="tactivity"),
    path("students/",views.students,name="students"),
    path("sroom/<str:pk>/rstudents/",views.rstudents,name="rstudents"),
    path("troom/<str:pk>/trstudents/",views.trstudents,name="trstudents"),

    path('sroom/<str:pk>/',views.sroom,name="sroom"),
    path('troom/<str:pk>/',views.troom,name='troom'),
    path('create_room/',views.create_room,name='create-room'),
    path('logout_student/',views.LogOutStudent,name="logout-student"),
    path('logout_teacher/',views.LogOutTeacher,name="logout-teacher"),

    #update / view profile
    path('studentProfile/',views.studentProfile,name='studentProfile'),
    path('ProfessorProfile/',views.ProfessorProfile,name='ProfessorProfile'),
    path('studentprofileupdate/',views.studentprofileupdate,name='studentprofileupdate'),
    path('Professorprofileupdate/',views.Professorprofileupdate,name='Professorprofileupdate'),




]