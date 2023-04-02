from django.shortcuts import render, redirect,get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import User ,Teacher,Student,Room,Message
from base import models
from .forms import StudentRegisterForm,TeacherRegisterForm,StudentUpdateForm,TeacherUpdateForm,UserForm,CreateRoomForm

@login_required(login_url='check')
def portal(request):
    return render(request,'base/portal.html',{})

@login_required(login_url='check')
def student_room(request):

    Student_User=get_object_or_404(Student,user=request.user)
    rooms=Student_User.rooms.all

    context={'rooms':rooms}
    return render(request,'base/student_room.html',context)

@login_required(login_url='check')
def teacher_room(request):
    # Teacher_User=Teacher.objects.get(user=request.user)
    Teacher_User=get_object_or_404(Teacher, user=request.user)
    rooms=Teacher_User.rooms.all
    context={'rooms':rooms}
    return render(request,'base/teacher_room.html',context)


def LandingPage(request):
    return render(request,'base/landingpage.html',{})

def check(request):
    return render(request,'base/check.html',{})

def StudentLogin(request):
    # if request.user.is_authenticated:
    #     return redirect('portal')
    
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')

        # try:
        #     user=User.objects.get(email=email)
        # except:
        #     messages.error(request, 'User does not exist!!')
        
        # user = authenticate(request, email=email, password=password)

        # if user is not None:
        #     login(request, user)
        #     return redirect('portal')
        # else:
        #     messages.error(request, 'Username OR password does not exit')

        if user := authenticate(username=username, password=password):
            if user.is_active:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                return redirect('student-room')

            else:
                return HttpResponse("Account not active")

        else:
            messages.error(request, "Invalid Details")
            return redirect('student-login')
    return render(request,'base/login_student.html',{})

#TeacherLogin

def LogOutStudent(request):
    logout(request)
    return redirect('landingpage')

def LogOutTeacher(request):
    logout(request)
    return redirect('landingpage')


def StudentRegister(request):
    user_type="student"
    # form = StudentRegisterForm()

    if request.method == 'POST':
        student_form = StudentRegisterForm(request.POST)
        user_form=UserForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            # if user_form.DoesNotExist:
                user=user_form.save(commit=False)
                user.is_student=True
                user.save()

                profile=student_form.save(commit=False)
                profile.user=user
                profile.save()
                return redirect('student-room')
            # else:
                messages.error(request,'User already exists with this mailID')
        else:
            messages.error(request,'An error occured during Student Registration')
    else:
        user_form=UserForm()
        student_form=StudentRegisterForm()

    context={'user_form':user_form,'student_form':student_form}

    return render(request,'base/student_register.html',context)

def TeacherRegister(request):
    user_type="student"
    # form = StudentRegisterForm()

    if request.method == 'POST':
        Teacher_form = TeacherRegisterForm(request.POST)
        user_form=UserForm(request.POST)
        if user_form.is_valid() and Teacher_form.is_valid():
            # if user_form.DoesNotExist:
                user=user_form.save(commit=False)
                user.is_teacher=True
                user.save()

                profile=Teacher_form.save(commit=False)
                profile.user=user
                profile.save()
                return redirect('teacher-login')
            # else:
                messages.error(request,'User already exists with this mailID')
        else:
            messages.error(request,'An error occured during Teacher Registration')
    else:
        user_form=UserForm()
        Teacher_form=TeacherRegisterForm()

    context={'user_form':user_form,'teacher_form':Teacher_form}

    return render(request,'base/teacher_register.html',context)




def TeacherLogin(request):
    # if request.user.is_authenticated:
    #     return redirect('portal')
    
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')

        # try:
        #     user=User.objects.get(email=email)
        # except:
        #     messages.error(request, 'User does not exist!!')
        
        # user = authenticate(request, email=email, password=password)

        # if user is not None:
        #     login(request, user)
        #     return redirect('portal')
        # else:
        #     messages.error(request, 'Username OR password does not exit')

        if user := authenticate(username=username, password=password):
            if user.is_active:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                return redirect('teacher-room')

            else:
                return HttpResponse("Account not active")

        else:
            messages.error(request, "Invalid Details")
            return redirect('teacher-login')
    return render(request,'base/login_teacher.html',{})




def create_room(request):
    form=CreateRoomForm()
    # Teacher_User=request.user.Teacher
    Teacher_User=get_object_or_404(Teacher, user=request.user)

    if request.method == 'POST':

        new_room=Room.objects.create(
            avatar=request.POST.get('avatar'),
            course_id=request.POST.get('course_id'),
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            room_code=request.POST.get('room_code'),
            # room=request.POST.get('room_id'),
            teacher=Teacher_User.name,
        )
        Teacher_User.rooms.add(new_room)
        return redirect('teacher-room')

    context={'form':form}

    return render(request, 'base/create_room.html',context)

@csrf_protect
def Join(request):

    Student_User=get_object_or_404(Student, user=request.user)

    rooms=Room.objects.all()

    if request.method=='POST':
        room_id=request.POST.get('room_id')
        code=request.POST.get('code')
        room=Room.objects.get(id=room_id)
        print('checkingg...')
        if (code==room.room_code):

            Student_User.rooms.add(room)
        
        else:
            messages.error(request,"Code don't match !!!")
 
    context={'rooms':rooms}
    return render(request,'base/join_room.html',context)

def sroom(request ,pk):
    room=Room.objects.get(id=pk)
    room_messages=room.message_set.all()
    participants=Student.objects.filter(rooms__id=pk)

    if request.method=='POST':
        message=Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        return redirect('sroom',pk=room.id)
    
    context={'room':room,'room_messages':room_messages,'participants':participants}

    return render(request,'base/sroom.html',context)


def troom(request ,pk):
    room=Room.objects.get(id=pk)
    room_messages=room.message_set.all()

    if request.method =='POST':
        message=Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        return redirect('troom',pk=room.id)
    
    context={'room':room,'room_messages':room_messages}

    return render(request,'base/troom.html',context)

@login_required(login_url='check')
def sactivity(request):
    messages=Message.objects.filter(user=request.user)

    context={'messages':messages}

    return render(request,'base/sactivity.html',context)

def students(request):
    students=Student.objects.all()

    context={'students':students}

    return render(request,'base/students.html',context)

def rstudents(request, pk):
    room=Room.objects.get(id=pk)

    students=Student.objects.filter(rooms__id=pk)

    context={'room':room,'students':students}

    return render(request,'base/rstudents.html',context)


def trstudents(request,pk):
    room=Room.objects.get(id=pk)

    students=Student.objects.filter(rooms__id=pk)

    context={'room':room,'students':students}

    return render(request,'base/trstudents.html',context)