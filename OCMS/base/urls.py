from django.urls import path
from . import views

urlpatterns=[
    path("",views.LandingPage,name="landingpage"),
    path("check/",views.check,name="check"),

    #temporary
    path("portal/",views.portal,name="portal"),

    path("login_student/",views.StudentLogin,name="student-login"),
    path("register_student/",views.StudentRegister,name="student-register"),
    # path("register_teacher/",views.TeacherRegister,name="teacher-register"),
    # path("login_teacher/",views.TeacherLogin,name="teacher-login"),
    # path('room/<str:pk>/',views.room,name="room"),
    # path('classroom/<str:pk>/',views.ClassRoom,name="classroom"),
    # path('teacher_room/',views.TeacherRoom,name='teacher-room'),
    # path('logout_student/',views.LogOutStudent,name="logout-student"),
    # path('logout_teacher/',views.LogOutTeacher,name="logout-teacher"),



]