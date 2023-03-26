from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User ,Teacher,Student,Room,Message
from .forms import StudentRegisterForm,TeacherRegisterForm,RoomForm,StudentUpdateForm,TeacherUpdateForm

def LandingPage(request):
    return render(request,'base/landingpage.html',{})

def check(request):
    return render(request,'base/check.html',{})

def StudentLogin(request):
    if request.user.is_authenticated:
        return redirect('portal')
    
    if request.method=='POST':
        email=request.POST.get('email')
        password = request.POST.get('password')

        try:
            user=User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist!!')
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('portal')
        else:
            messages.error(request, 'Username OR password does not exit')

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
    form = StudentRegisterForm()

    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student=True
            user.save()
            login(request,user)
            return redirect('portal')
        else:
            messages.error(request,'An error occured during Student Registration')

    return render(request,'base/student_register.html',{'form':form,'user_type':user_type})

def TeacherRegister(request):
    user_type="teacher"
    form = TeacherRegisterForm()

    if request.method == 'POST':
        form = TeacherRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_teacher=True
            user.save()
            login(request,user)
            return redirect('portal')
        else:
            messages.error(request,'An error occured during Teacher Registration')

    return render(request,'base/teacher_register.html',{'form':form,'user_type':user_type})


def room(request,pk):
    room=Room.objects.get(id=pk)
    room_messages=room.message_set.all()
    # students=room.students.all()
    students=std(room)

    if request.method == 'POST':
        message=Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        #adding students to be sorted
        return redirect('room',pk=room.id)
    
    context={'room':room,'room_messages':room_messages,'students':students}

    return render(request,'base/room.html',context)

def std(self,request):
    rooms=request.GET.get('rooms')

    result = Student.objects.filter(
        rooms=rooms
    )
    return result











